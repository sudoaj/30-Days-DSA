#!/bin/bash

# Set the Django settings module environment variable
export DJANGO_SETTINGS_MODULE=Wordle.settings

# Run the Django shell and execute Python code to create players
python manage.py shell <<EOF
from random import randint
from django.contrib.auth.models import User
from frontend.models import Player

# Iterate over all users in the database
users = User.objects.all()

for user in users:
    # Check if a Player already exists for the user
    if not Player.objects.filter(player=user).exists():
        # Generate random stats
        games_played = randint(0, 100)
        games_won = randint(0, games_played)
        win_streak = randint(0, games_won)

        # Create the Player
        Player.objects.create(
            player=user,
            games_played=games_played,
            games_won=games_won,
            win_streak=win_streak
        )

        print(f"Created Player for user: {user.username}")
    else:
        print(f"Player already exists for user: {user.username}")
EOF
