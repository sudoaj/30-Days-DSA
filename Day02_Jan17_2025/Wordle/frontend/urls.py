from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),                  # Home page
    path('todays-game/', views.todays_game, name='todays_game'),  # Today's game
    path('validate-guess/', views.validate_guess, name='validate_guess'),

    # path('submit-guess/', views.submit_guess, name='submit_guess'),
    # path('game-over/<str:status>/', views.game_over, name='game_over'),
]