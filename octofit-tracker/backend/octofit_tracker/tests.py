from django.test import TestCase
from .models import Team, User, Activity, Workout, Leaderboard

class BasicModelTest(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(str(team), 'Test Team')

    def test_user_creation(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create_user(username='testuser', email='test@example.com', password='testpass', team=team)
        self.assertEqual(user.email, 'test@example.com')

    def test_activity_creation(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create_user(username='testuser', email='test@example.com', password='testpass', team=team)
        activity = Activity.objects.create(user=user, type='run', duration=10, distance=2.5)
        self.assertEqual(activity.type, 'run')

    def test_workout_creation(self):
        team = Team.objects.create(name='Test Team')
        workout = Workout.objects.create(name='W1', description='desc', team=team)
        self.assertEqual(workout.name, 'W1')

    def test_leaderboard_creation(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create_user(username='testuser', email='test@example.com', password='testpass', team=team)
        leaderboard = Leaderboard.objects.create(user=user, points=50)
        self.assertEqual(leaderboard.points, 50)
