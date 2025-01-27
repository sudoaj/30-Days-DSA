#!/bin/bash

set -e  # Exit the script if any command fails

echo "Resetting migrations..."
./1_reset_migrations.sh
echo "Migrations reset successfully."

echo "Creating superuser..."
./2_create_super_user.sh
echo "Superuser created successfully."

echo "Creating users..."
./3_create_user.sh
echo "User created successfully."

echo "Creating players..."
./4_create_player.sh
echo "Players created successfully."

echo "Creating daily word..."
./5_create_words.sh
echo "Daily word created successfully."


echo "All tasks completed successfully."

# Run the Django development server
python manage.py runserver 127.0.0.1:8000




