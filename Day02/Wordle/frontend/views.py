from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.utils.timezone import now
from .models import DailyWord, Guess, GameSession


def home(request):
    """
    Displays the home page with a 'Play Now' button.
    """
    # Get today's daily word
    today = now().date()
    daily_word = DailyWord.objects.filter(date=today).first()

    # If no word exists for today, show an error on the home page
    if not daily_word:
        return render(request, 'frontend/home.html', {
            'error_message': 'No word available for today! Please check back later.'
        })

    # Ensure the user has an associated Player instance
    if not hasattr(request.user, 'player'):
        return render(request, 'frontend/home.html', {
            'error_message': 'You are not a registered player!'
        })

    # Render the home page with the Play Now button
    return render(request, 'frontend/home.html', {})

def todays_game(request):
    """
    Unified view for today's game, handling both game display and guess submissions.
    """
    # Get today's daily word
    today = now().date()
    daily_word = DailyWord.objects.filter(date=today).first()

    # If no word exists for today, show an error
    if not daily_word:
        return render(request, 'frontend/todays_game.html', {
            'error_message': 'No word available for today!',
            'daily_word': None,
            'guesses': None,
            'max_attempts': None,
            'status': None,
        })

    # Ensure the user has an associated Player instance
    if not hasattr(request.user, 'player'):
        return render(request, 'frontend/todays_game.html', {
            'error_message': 'You are not a registered player!',
            'daily_word': None,
            'guesses': None,
            'max_attempts': None,
            'status': None,
        })

    # Fetch the Player instance
    player = request.user.player

    # Handle POST request for guesses
    if request.method == 'POST':
        guess_word = request.POST.get('guess')

        # Check if guess is valid
        if not guess_word or len(guess_word) != 5:
            return JsonResponse({'error': 'Invalid guess! Please enter a 5-letter word.'}, status=400)

        # Check if the guess is correct
        is_correct = guess_word.lower() == daily_word.word.lower()

        # Record the guess
        Guess.objects.create(
            player=player,
            daily_word=daily_word,
            guess=guess_word,
            attempt=Guess.objects.filter(player=player, daily_word=daily_word).count() + 1
        )

        # Handle game outcome
        if is_correct:
            return JsonResponse({'message': 'Correct!', 'status': 'won'})
        elif Guess.objects.filter(player=player, daily_word=daily_word).count() >= 6:  # Max attempts reached
            return JsonResponse({'message': 'Game Over!', 'status': 'lost'})
        else:
            return JsonResponse({'message': 'Try Again!', 'status': 'continue'})

    # Handle GET request to display the game
    guesses = Guess.objects.filter(player=player, daily_word=daily_word).order_by('attempt')
    max_attempts = 6
    remaining_attempts = max_attempts - guesses.count()

    return render(request, 'frontend/todays_game.html', {
        'error_message': None,
        'daily_word': daily_word.word,
        'guesses': guesses,
        'max_attempts': max_attempts,
        'remaining_attempts': remaining_attempts,
        'status': None,
    })
# def todays_game(request):
#     """
#     Displays the main game page for today's word.
#     """
#     # Get today's daily word
#     today = now().date()
#     daily_word = DailyWord.objects.filter(date=today).first()

#     # If no word exists for today, show an error
#     if not daily_word:
#         return render(request, 'frontend/error.html', {'message': 'No word available for today!'})

#     # Ensure the user has an associated Player instance
#     if not hasattr(request.user, 'player'):
#         return render(request, 'frontend/error.html', {'message': 'You are not a registered player!'})

#     # Fetch the Player instance
#     player = request.user.player

#     # Fetch the player's guesses (if any)
#     guesses = Guess.objects.filter(
#         player=player,
#         daily_word=daily_word
#     ).order_by('attempt')

#     return render(request, 'frontend/todays_game.html', {
#         'daily_word': daily_word,
#         'guesses': guesses,
#         'max_attempts': 6  # Assuming a maximum of 6 attempts
#     })


# def submit_guess(request):
#     if request.method == 'POST':
#         guess_word = request.POST.get('guess')
#         daily_word = DailyWord.objects.filter(date=now().date()).first()

#         if not daily_word:
#             return JsonResponse({'error': 'No word available for today!'}, status=400)

#         # Ensure the user has an associated Player instance
#         if not hasattr(request.user, 'player'):
#             return JsonResponse({'error': 'You are not a registered player!'}, status=400)

#         # Fetch the Player instance
#         player = request.user.player

#         # Check if guess is correct
#         is_correct = guess_word.lower() == daily_word.word.lower()

#         # Record the guess
#         guess = Guess.objects.create(
#             player=player,
#             daily_word=daily_word,
#             guess=guess_word,
#             attempt=Guess.objects.filter(player=player, daily_word=daily_word).count() + 1
#         )

#         # Return feedback
#         if is_correct:
#             return JsonResponse({'message': 'Correct!', 'status': 'won'})
#         elif guess.attempt >= 6:  # Max attempts reached
#             return JsonResponse({'message': 'Game Over!', 'status': 'lost'})
#         else:
#             return JsonResponse({'message': 'Try Again!', 'status': 'continue'})

#     return JsonResponse({'error': 'Invalid request'}, status=400)


# def game_over(request, status):
#     daily_word = DailyWord.objects.filter(date=now().date()).first()
#     return render(request, 'frontend/game_over.html', {
#         'status': status,
#         'daily_word': daily_word.word if daily_word else 'Unknown'
#     })



