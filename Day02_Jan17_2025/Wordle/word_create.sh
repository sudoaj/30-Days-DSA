#!/bin/bash

# Set the Django settings module environment variable
export DJANGO_SETTINGS_MODULE=Wordle.settings

# Run the Django shell and execute Python code to create a valid 5-letter daily word
python manage.py shell <<EOF
import random
from django.utils.timezone import now
from frontend.models import DailyWord

# Predefined list of valid 5-letter English words
VALID_WORDS = [
    "apple", "grape", "pearl", "stone", "light",
    "proud", "globe", "brave", "chair", "plant",
    "trend", "solar", "ocean", "crown", "charm",
    "vivid", "flare", "spark", "frame", "river",
    "plane", "flint", "grind", "smile", "bread",
    "cloud", "storm", "field", "grain", "scale",
    "swift", "power", "union", "lunar", "jolly",
    "giant", "frost", "pride", "crisp", "flame",
    "woven", "trust", "sight", "blast", "flown",
    "sharp", "jewel", "drive", "spend", "chart",
    "trace", "glove", "vocal", "blend", "shard",
    "beach", "crest", "clear", "flock", "grasp",
    "shine", "climb", "spice", "hover", "quiet",
    "whale", "zebra", "glide", "brand", "dream",
    "steep", "fence", "solid", "quick", "humor",
    "angle", "heart", "grill", "limit", "blink",
    "voice", "straw", "prune", "chime", "slice",
    "adorn", "burst", "probe", "chill", "sound",
    "paint", "arise", "crane", "forge", "gravy",
    "clerk", "shrew", "naval", "perky", "folly"
]

# Get today's date
today = now().date()

# Check if a DailyWord already exists for today
if DailyWord.objects.filter(date=today).exists():
    print(f"A daily word already exists for {today}.")
else:
    # Select a random word from the valid list
    word = random.choice(VALID_WORDS)
    DailyWord.objects.create(word=word, date=today, is_active=True)
    print(f"Created new daily word: {word} for {today}")
EOF