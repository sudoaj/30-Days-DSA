#!/bin/bash


# Set environment variables for the superuser
DJANGO_SUPERUSER_USERNAME=aj
DJANGO_SUPERUSER_EMAIL=aj@aj.com
DJANGO_SUPERUSER_PASSWORD=Elon2020?

# Run the Django shell to create the superuser
echo "
from django.contrib.auth import get_user_model

User = get_user_model()
if not User.objects.filter(username='$DJANGO_SUPERUSER_USERNAME').exists():
    User.objects.create_superuser(
        username='$DJANGO_SUPERUSER_USERNAME',
        email='$DJANGO_SUPERUSER_EMAIL',
        password='$DJANGO_SUPERUSER_PASSWORD'
    )
    print('Superuser created successfully.')
else:
    print('Superuser already exists.')
" | python manage.py shell