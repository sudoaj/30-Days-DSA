#!/bin/bash

set -e  # Exit the script if any command fails

echo "Resetting migrations..."
./reset_migrations.sh
echo "Migrations reset successfully."

echo "Creating superuser..."
./create_superuser.sh
echo "Superuser created successfully."


echo "Creating players..."
./players_create.sh
echo "Players created successfully."

echo "Creating daily word..."
./word_create.sh
echo "Daily word created successfully."


echo "All tasks completed successfully."

# Run the Django development server
python manage.py runserver 0.0.0.0:8000


