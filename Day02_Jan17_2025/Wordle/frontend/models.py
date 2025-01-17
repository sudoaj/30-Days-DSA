from django.db import models
from django.contrib.auth.models import User

class DailyWord(models.Model):
    """
    Stores the word for each day.
    """
    word = models.CharField(max_length=5, unique=True)  # Assuming 5-letter words
    date = models.DateField(unique=True)  # To ensure one word per day
    is_active = models.BooleanField(default=False)  # Optional: for marking the active word

    def __str__(self):
        return f"{self.word} ({self.date})"


class Player(models.Model):
    """
    Stores player information and game stats.
    """
    player = models.OneToOneField(User, on_delete=models.CASCADE, related_name='player')
    games_played = models.PositiveIntegerField(default=0)
    games_won = models.PositiveIntegerField(default=0)
    win_streak = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.player.username


class Guess(models.Model):
    """
    Tracks each guess made by a player for a specific word.
    """
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='guesses')
    daily_word = models.ForeignKey(DailyWord, on_delete=models.CASCADE, related_name='guesses')
    guess = models.CharField(max_length=5)  # Assuming 5-letter guesses
    attempt = models.PositiveIntegerField()  # Tracks which attempt this is
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.player.username} guessed {self.guess} for {self.daily_word.word}"


class GameSession(models.Model):
    """
    Tracks a player's session for each daily word.
    """
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='game_sessions')
    daily_word = models.ForeignKey(DailyWord, on_delete=models.CASCADE, related_name='game_sessions')
    completed = models.BooleanField(default=False)  # If the game was completed
    won = models.BooleanField(default=False)  # If the player won
    attempts = models.PositiveIntegerField(default=0)  # Number of attempts taken

    def __str__(self):
        return f"Game: {self.player.username} - {self.daily_word.date} ({'Won' if self.won else 'Lost'})"