from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.utils.timezone import now
from frontend.models import DailyWord, Guess, Player


class WordleAppTests(TestCase):
    def setUp(self):
        """
        Set up the test environment with a user, player, daily word, and client.
        """
        # Create a test user and login
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.client = Client()
        self.client.login(username="testuser", password="password123")

        # Create a Player instance for the user
        self.player = Player.objects.create(player=self.user)

        # Create today's DailyWord
        self.daily_word = DailyWord.objects.create(word="APPLE", date=now().date())

    def test_home_view_with_word(self):
        """
        Test the home view when a daily word exists.
        """
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Play Now")

    def test_home_view_no_word(self):
        """
        Test the home view when no daily word exists.
        """
        self.daily_word.delete()
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No word available for today!")

    def test_home_view_no_player(self):
        """
        Test the home view when the user is not associated with a Player instance.
        """
        self.player.delete()
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "You are not a registered player!")

    def test_todays_game_view_with_word(self):
        """
        Test the today's game view when a daily word exists.
        """
        response = self.client.get("/todays-game/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.daily_word.word)

    def test_todays_game_view_no_word(self):
        """
        Test the today's game view when no daily word exists.
        """
        self.daily_word.delete()
        response = self.client.get("/todays-game/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No word available for today!")

    def test_todays_game_view_no_player(self):
        """
        Test the today's game view when the user is not associated with a Player instance.
        """
        self.player.delete()
        response = self.client.get("/todays-game/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "You are not a registered player!")

    def test_validate_guess_correct(self):
        """
        Test the validate_guess endpoint with a correct guess.
        """
        response = self.client.post(
            "/validate-guess/",
            data={"guess": "APPLE"},
            content_type="application/json",
            HTTP_X_REQUESTED_WITH="XMLHttpRequest",
        )
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertEqual(response_data["status"], "success")
        self.assertIn("Congratulations", response_data["message"])

    def test_validate_guess_incorrect(self):
        """
        Test the validate_guess endpoint with an incorrect guess.
        """
        response = self.client.post(
            "/validate-guess/",
            data={"guess": "GRAPE"},
            content_type="application/json",
            HTTP_X_REQUESTED_WITH="XMLHttpRequest",
        )
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertEqual(response_data["status"], "continue")
        self.assertIn("Try again", response_data["message"])

    def test_validate_guess_invalid_length(self):
        """
        Test the validate_guess endpoint with an invalid guess length.
        """
        response = self.client.post(
            "/validate-guess/",
            data={"guess": "TOO"},
            content_type="application/json",
            HTTP_X_REQUESTED_WITH="XMLHttpRequest",
        )
        self.assertEqual(response.status_code, 400)
        response_data = response.json()
        self.assertEqual(response_data["status"], "error")
        self.assertEqual(response_data["message"], "Invalid guess length!")

    def test_validate_guess_game_over(self):
        """
        Test the validate_guess endpoint when the player exceeds maximum attempts.
        """
        # Add 5 incorrect guesses
        for i in range(5):
            Guess.objects.create(player=self.player, daily_word=self.daily_word, guess="GRAPE", attempt=i + 1)

        # Submit the 6th incorrect guess
        response = self.client.post(
            "/validate-guess/",
            data={"guess": "MANGO"},
            content_type="application/json",
            HTTP_X_REQUESTED_WITH="XMLHttpRequest",
        )
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertEqual(response_data["status"], "game_over")
        self.assertIn("Game Over", response_data["message"])