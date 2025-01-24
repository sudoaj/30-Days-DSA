#!/bin/bash

# Set the Django settings module environment variable if necessary
export DJANGO_SETTINGS_MODULE=Wordle.settings  # Replace 'your_project' with your actual project name

# Run the Django shell and execute Python code to create 10 users with creative details
python manage.py shell <<EOF
import random
import string
from django.contrib.auth.models import User

# Random username generator
def random_username():
    adjectives = ["Brave", "Clever", "Swift", "Mighty", "Gentle", "Bold", "Quick", "Bright", "Lucky", "Strong"]
    nouns = ["Tiger", "Falcon", "Wolf", "Bear", "Lion", "Eagle", "Hawk", "Fox", "Panther", "Otter"]
    return f"{random.choice(adjectives)}{random.choice(nouns)}{random.randint(100, 999)}"

# Random email generator
def random_email(username):
    domains = ["example.com", "creativemail.com", "wordlegame.net", "testmail.org"]
    return f"{username.lower()}@{random.choice(domains)}"

# Random password generator
def random_password():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=12))

# Create 10 users with random details
for i in range(10):
    username = random_username()
    email = random_email(username)
    password = random_password()

    if not User.objects.filter(username=username).exists():
        User.objects.create_user(username=username, email=email, password=password)
        print(f"Created user: {username} | Email: {email} | Password: {password}")
    else:
        print(f"User {username} already exists!")
EOF