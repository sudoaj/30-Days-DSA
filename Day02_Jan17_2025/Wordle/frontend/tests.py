from django.test import TestCase, Client
from django.utils.timezone import now
from django.contrib.auth.models import User
from .models import DailyWord, Player, Guess

class FrontendTests(TestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='password')
        
        # Create a test player linked to the user
        self.player = Player.objects.create(player=self.user)
        
        # Create a daily word
        self.daily_word = DailyWord.objects.create(word='apple', date=now().date())

        # Log in the test user
        self.client = Client()
        self.client.login(username='testuser', password='password')

    def test_home_view(self):
        # Test the home view (GET)
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Play Now')

    def test_todays_game_view(self):
        # Test the today's game view (GET)
        response = self.client.get('/todays-game/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Daily Word')
        self.assertContains(response, 'Remaining Attempts')

    def test_submit_valid_guess(self):
        # Test submitting a valid guess
        response = self.client.post('/todays-game/', {'guess': 'apple'})
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content.decode(), {'message': 'Correct!', 'status': 'won'})

    def test_submit_invalid_guess(self):
        # Test submitting an invalid guess
        response = self.client.post('/todays-game/', {'guess': 'cat'})
        self.assertEqual(response.status_code, 400)
        self.assertContains(response, 'Invalid guess', status_code=400)

    def test_guess_limit_exceeded(self):
        # Submit multiple incorrect guesses to exceed limit
        for _ in range(6):
            self.client.post('/todays-game/', {'guess': 'wrong'})
        response = self.client.post('/todays-game/', {'guess': 'wrong'})
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content.decode(), {'message': 'Game Over!', 'status': 'lost'})

    def test_no_daily_word(self):
        # Remove the daily word and test behavior
        self.daily_word.delete()
        response = self.client.get('/todays-game/')
        self.assertContains(response, 'No word available for today!', status_code=200)