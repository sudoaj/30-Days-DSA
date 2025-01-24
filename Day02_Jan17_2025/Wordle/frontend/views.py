from django.shortcuts import render
from django.http import JsonResponse
from django.utils.timezone import now
from .models import DailyWord, Guess


def get_daily_word():
    """Helper function to fetch today's word."""
    today = now().date()
    return DailyWord.objects.filter(date=today).first()


def get_player(request):
    """Helper function to fetch the player instance for the current user."""
    return getattr(request.user, 'player', None)


def home(request):
    """
    Displays the home page with a 'Play Now' button.
    """
    daily_word = get_daily_word()

    if not daily_word:
        return render(request, 'frontend/home.html', {
            'error_message': 'No word available for today! Please check back later.'
        })

    if not get_player(request):
        return render(request, 'frontend/home.html', {
            'error_message': 'You are not a registered player!'
        })

    return render(request, 'frontend/home.html')


def todays_game(request):
    """
    Displays the game page for today's word.
    """
    daily_word = get_daily_word()

    if not daily_word:
        return render(request, 'frontend/todays_game.html', {
            'error_message': 'No word available for today!'
        })

    player = get_player(request)
    if not player:
        return render(request, 'frontend/todays_game.html', {
            'error_message': 'You are not a registered player!'
        })

    guesses = Guess.objects.filter(player=player, daily_word=daily_word).order_by('attempt')
    max_attempts = 5
    remaining_attempts = max_attempts - guesses.count()

    return render(request, 'frontend/todays_game.html', {
        'daily_word': daily_word.word,
        'guesses': guesses,
        'max_attempts': max_attempts,
        'remaining_attempts': remaining_attempts,
        'keys_row_one': list("QWERTYUIOP"),
        'keys_row_two': list("ASDFGHJKL"),
        'keys_row_three': ["⬅", "Z", "X", "C", "V", "B", "N", "M", "✅"],
        'word_length': len(daily_word.word),
        'num_guesses': range(5),
    })


def validate_guess(request):
    """
    Validates a player's guess and returns feedback.
    """
    if request.method == "POST":
        import json
        data = json.loads(request.body)
        guess = data.get("guess", "").lower()

        daily_word = get_daily_word()
        if not daily_word:
            return JsonResponse({"status": "error", "message": "No word available for today!"})

        if len(guess) != len(daily_word.word):
            return JsonResponse({"status": "error", "message": "Invalid guess length!"})

        target_word_list = list(daily_word.word.lower())
        guess_list = list(guess)
        result = ["absent"] * len(target_word_list)

        # First pass: Correct letters
        for i in range(len(guess_list)):
            if guess_list[i] == target_word_list[i]:
                result[i] = "correct"
                target_word_list[i] = None

        # Second pass: Present letters
        for i in range(len(guess_list)):
            if result[i] == "absent" and guess_list[i] in target_word_list:
                result[i] = "present"
                target_word_list[target_word_list.index(guess_list[i])] = None

        player = get_player(request)
        Guess.objects.create(
            player=player,
            daily_word=daily_word,
            guess=guess,
            attempt=Guess.objects.filter(player=player, daily_word=daily_word).count() + 1
        )

        if guess == daily_word.word.lower():
            return JsonResponse({
                "status": "success",
                "message": "Congratulations! You've guessed the word!",
                "result": result,
            })

        if Guess.objects.filter(player=player, daily_word=daily_word).count() >= 6:
            return JsonResponse({
                "status": "game_over",
                "message": f"Game Over! The correct word was: {daily_word.word}",
                "result": result,
            })

        return JsonResponse({
            "status": "continue",
            "message": "Try again!",
            "result": result,
        })

    return JsonResponse({"status": "error", "message": "Invalid request!"})