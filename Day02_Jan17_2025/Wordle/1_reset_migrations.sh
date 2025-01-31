#!/bin/bash

# Navigate to the project directory

echo "Deleting migrations for the 'frontend' app..."
find frontend/migrations -type f -name "*.py" ! -name "__init__.py" -delete

echo "Deleting the SQLite database..."
rm -f db.sqlite3

echo "Recreating initial migrations..."
python manage.py makemigrations

echo "Applying migrations..."
python manage.py migrate

echo "All previous migrations and database have been deleted and reset!"