from django.urls import path
from . import views

urlpatterns = [
    # Home Page
    path('', views.home, name='home'),

    # Today's Game
    path('todays-game/', views.todays_game, name='todays_game'),

    # Validate Guess (API endpoint)
    path('validate-guess/', views.validate_guess, name='validate_guess'),

    # Optional Routes (Commented)
    # path('submit-guess/', views.submit_guess, name='submit_guess'),
    # path('game-over/<str:status>/', views.game_over, name='game_over'),

    # Error Page
    path('error/', views.error, name='error'),  # For displaying custom error messages
]