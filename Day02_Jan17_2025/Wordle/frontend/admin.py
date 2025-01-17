from django.contrib import admin
from .models import DailyWord, Player, Guess, GameSession

admin.site.register(DailyWord)
admin.site.register(Player)
admin.site.register(Guess)
admin.site.register(GameSession)