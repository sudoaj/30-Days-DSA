#!/bin/bash

# Exit on errors
set -e

# Check for required arguments
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <project_name> <app_name>"
    exit 1
fi

PROJECT_NAME=$1
APP_NAME=$2

echo "Setting up Django project: $PROJECT_NAME with app: $APP_NAME"
# Create the project directory
mkdir $PROJECT_NAME
cd $PROJECT_NAME

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Upgrade pip and install Django
pip install --upgrade pip
pip install django

# Save dependencies to requirements.txt
pip freeze > requirements.txt

# Create Django project
django-admin startproject config .


# Create the specified app
python manage.py startapp $APP_NAME

# Create 'accounts' app for custom user authentication
python manage.py startapp accounts

# Add apps to INSTALLED_APPS in settings.py
SETTINGS_FILE="config/settings.py"

# Check if the script is running on macOS
if [[ "$OSTYPE" == "darwin"* ]]; then
    sed -i '' "/INSTALLED_APPS = \[/ a\\
    '$APP_NAME',\\
    'accounts',
    " $SETTINGS_FILE
else
    sed -i "/INSTALLED_APPS = \[/ a\    '$APP_NAME',\n    'accounts'," $SETTINGS_FILE
fi

# Configure the custom user model
cat <<EOL > accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    pass
EOL

# Register the custom user model in accounts/admin.py
cat <<EOL > accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

admin.site.register(CustomUser, UserAdmin)
EOL

# Update settings.py to use custom user model
echo "AUTH_USER_MODEL = 'accounts.CustomUser'" >> $SETTINGS_FILE

# Create a global templates directory inside the Django project
mkdir -p config/templates accounts/templates/accounts

# Ensure settings.py is updated to include the templates directory
cat <<EOL >> $SETTINGS_FILE

# Update TEMPLATES DIRS to include the global templates folder
import os
TEMPLATES[0]['DIRS'] = [os.path.join(BASE_DIR, "templates")]
EOL

# Create a Bootstrap-styled homepage inside the correct template directory
cat <<EOL > accounts/templates/accounts/index.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container">
            <a class="navbar-brand" href="#">$PROJECT_NAME</a>
            <div class="collapse navbar-collapse">
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item"><a class="nav-link" href="{% url 'login' %}">Login</a></li>
                    <li class="nav-item"><a class="nav-link" href="{% url 'register' %}">Register</a></li>
                </ul>
            </div>
        </div>
    </nav>
    <div class="container mt-5">
        <div class="jumbotron bg-light p-5">
            <h1 class="display-4">Welcome to $PROJECT_NAME</h1>
            <p class="lead">This is a simple Django app with user authentication.</p>
            <a class="btn btn-primary btn-lg" href="{% url 'register' %}" role="button">Get Started</a>
        </div>
    </div>
</body>
</html>
EOL

# Create login page
cat <<EOL > accounts/templates/accounts/login.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <div class="container mt-5">
        <h2>Login</h2>
        <form method="post">
            {% csrf_token %}
            {{ form.as_p }}
            <button type="submit" class="btn btn-primary">Login</button>
        </form>
        <p>Don't have an account? <a href="{% url 'register' %}">Register here</a></p>
    </div>
</body>
</html>
EOL

# Create register page
cat <<EOL > accounts/templates/accounts/register.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Register</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <div class="container mt-5">
        <h2>Register</h2>
        <form method="post">
            {% csrf_token %}
            {{ form.as_p }}
            <button type="submit" class="btn btn-success">Register</button>
        </form>
    </div>
</body>
</html>
EOL

# Create views for authentication
cat <<EOL > accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout

def home(request):
    return render(request, "accounts/index.html")

def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
    else:
        form = AuthenticationForm()
    return render(request, "accounts/login.html", {"form": form})

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = UserCreationForm()
    return render(request, "accounts/register.html", {"form": form})
EOL

# Create urls.py for accounts app
cat <<EOL > accounts/urls.py
from django.urls import path
from .views import user_login, register

urlpatterns = [
    path("login/", user_login, name="login"),
    path("register/", register, name="register"),
]
EOL

# Register URLs in project
cat <<EOL >> config/urls.py
from django.urls import path, include
from accounts.views import home

urlpatterns = [
    path("", home, name="home"),
    path("accounts/", include("accounts.urls")),
]
EOL

# Apply migrations
python manage.py makemigrations accounts
python manage.py migrate

# Create a superuser and a demo user
python manage.py shell <<EOF
from accounts.models import CustomUser

if not CustomUser.objects.filter(username="admin").exists():
    CustomUser.objects.create_superuser("admin", "admin@example.com", "AdminPassword123")

if not CustomUser.objects.filter(username="demo").exists():
    CustomUser.objects.create_user("demo", "user@example.com", "DemoPassword123")
EOF

# Run the development server
python manage.py runserver

echo "Django project $PROJECT_NAME is set up successfully!"
echo "Superuser: admin / admin@example.com / AdminPassword123"
echo "Demo user: demo / user@example.com / DemoPassword123"
echo "Requirements saved in requirements.txt"