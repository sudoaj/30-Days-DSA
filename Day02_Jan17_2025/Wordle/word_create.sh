#!/bin/bash


# Set the Django settings module environment variable
export DJANGO_SETTINGS_MODULE=Wordle.settings

# Run the Django shell and execute Python code to create a random daily word
python manage.py shell <<EOF
import random
import string
from django.utils.timezone import now
from frontend.models import DailyWord

# Generate a random 5-letter word
def generate_random_word():
    return ''.join(random.choices(string.ascii_lowercase, k=5))

# Get today's date
today = now().date()

# Check if a DailyWord already exists for today
if DailyWord.objects.filter(date=today).exists():
    print(f"A daily word already exists for {today}.")
else:
    # Generate and save a new daily word
    word = generate_random_word()
    DailyWord.objects.create(word=word, date=today, is_active=True)
    print(f"Created new daily word: {word} for {today}")
EOF