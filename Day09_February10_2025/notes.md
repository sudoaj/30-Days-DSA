# Django Project Automation Notes

## **Overview**
This document outlines the process of automating the creation of a Django project using a shell script. The script sets up a Django project, configures authentication, and creates a structured environment with Bootstrap-styled templates.

---

## **Steps Implemented in the Script**
### **1. Project Initialization**
- The script takes two arguments:
  - **Project Name** (e.g., `TestProj`)
  - **App Name** (e.g., `Wordle`)
- It creates a directory for the project and initializes a **virtual environment**.
- Installs Django and saves dependencies to `requirements.txt`.

### **2. Project Structure**
- The **Django project is created with `config/` as the settings folder** instead of using the project name.
- The script runs:
  ```bash
  django-admin startproject config .
  ```
  This ensures `config/` is correctly created inside the project directory.

### **3. App Creation**
- Two apps are created:
  - **User-defined app** (e.g., `Wordle`)
  - **`accounts` app** for authentication (custom user model and authentication views)

### **4. Configuration Adjustments**
- The **settings file is updated** to:
  - Include `config/templates/` as a template directory.
  - Use a **custom user model** (`accounts.CustomUser`).
  - Register the newly created apps (`Wordle`, `accounts`).
- URLs are registered correctly:
  - `config/urls.py` is modified to include `home`, `login`, and `register` routes.

### **5. Authentication System Setup**
- **Custom User Model** (`CustomUser`) extends Django’s `AbstractUser`.
- **Admin registration** is set up.
- **Views for authentication** (`login`, `register`, `home`) are created.
- **HTML templates for authentication pages** are added with Bootstrap styling.

### **6. Fixing Import Issues**
- **Ensured `home` view exists in `accounts/views.py`**
- **Fixed `config/urls.py` import issues** to prevent Django from failing due to missing references.

### **7. Database Migrations & Superuser Creation**
- The script runs Django migrations:
  ```bash
  python manage.py makemigrations accounts
  python manage.py migrate
  ```
- Automatically creates:
  - **Superuser:** `admin@example.com` / `AdminPassword123`
  - **Demo user:** `user@example.com` / `DemoPassword123`

### **8. Running the Server**
- The Django development server is automatically started using:
  ```bash
  python manage.py runserver
  ```

---

## **Final Project Structure**
```
TestProj/
│── config/                # Django settings and main project configuration
│   ├── settings.py        # Updated settings file
│   ├── urls.py            # URL routing
│── accounts/              # Authentication app
│   ├── models.py          # Custom user model
│   ├── views.py           # Login, register, home views
│   ├── urls.py            # Authentication URLs
│   ├── templates/
│       └── accounts/
│           ├── index.html     # Home page
│           ├── login.html     # Login page
│           ├── register.html  # Register page
│── Wordle/                # User-defined app
│── venv/                  # Virtual environment
│── requirements.txt       # Installed dependencies
│── manage.py              # Django CLI script
```

---

## **Commands to Run**
```bash
./setup_django.sh TestProj Wordle
```

This command will:
- Create a structured Django project.
- Set up authentication with a custom user model.
- Generate Bootstrap-styled login, register, and homepage templates.
- Apply migrations and create demo users.
- Start the development server.

---

## **Next Steps**
- Add more security measures (password validation, session timeout, etc.).
- Integrate PostgreSQL instead of SQLite.
- Extend `CustomUser` with additional fields (e.g., profile pictures, roles).
- Implement user email verification.
- Create an API for authentication (Django REST Framework).

This script automates Django project setup efficiently, making it easy to start new projects with authentication out-of-the-box! 🚀

