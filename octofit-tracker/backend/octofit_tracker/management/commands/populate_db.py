from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
<<<<<<< HEAD
from django.conf import settings
from pymongo import MongoClient
from datetime import timedelta
from bson import ObjectId

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activity, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Add debug output to confirm script execution
        print("Debug: populate_db.py script is being executed")

        # Connect to MongoDB
        client = MongoClient(settings.DATABASES['default'].get('HOST', 'localhost'), settings.DATABASES['default'].get('PORT', 27017))
        db = client[settings.DATABASES['default']['NAME']]

        # Drop existing collections
        db.users.drop()
        db.teams.drop()
        db.activity.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Create users
        users = [
            {"_id": ObjectId(), "username": "thundergod", "email": "thundergod@mhigh.edu", "password": "thundergodpassword"},
            {"_id": ObjectId(), "username": "metalgeek", "email": "metalgeek@mhigh.edu", "password": "metalgeekpassword"},
            {"_id": ObjectId(), "username": "zerocool", "email": "zerocool@mhigh.edu", "password": "zerocoolpassword"},
            {"_id": ObjectId(), "username": "crashoverride", "email": "crashoverride@hmhigh.edu", "password": "crashoverridepassword"},
            {"_id": ObjectId(), "username": "sleeptoken", "email": "sleeptoken@mhigh.edu", "password": "sleeptokenpassword"},
        ]
        db.users.insert_many(users)

        # Add more collections (teams, activities, leaderboard, workouts) as needed

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
=======

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Add error handling for data population
        try:
            # Add test data for users
            user1 = User.objects.create(email='testuser1@example.com', name='Test User 1')
            user2 = User.objects.create(email='testuser2@example.com', name='Test User 2')

            # Add test data for teams
            team1 = Team.objects.create(name='Team Alpha')
            team2 = Team.objects.create(name='Team Beta')
            team1.members.add(user1, user2)
            team2.members.add(user2)

            # Add test data for activities
            Activity.objects.create(user=user1, description='Running', date='2025-04-29T10:00:00Z')
            Activity.objects.create(user=user2, description='Cycling', date='2025-04-29T11:00:00Z')

            # Add test data for leaderboard
            Leaderboard.objects.create(user=user1, score=100)
            Leaderboard.objects.create(user=user2, score=80)

            # Add test data for workouts
            Workout.objects.create(name='Push-ups', duration=30)
            Workout.objects.create(name='Sit-ups', duration=20)

            self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data'))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f'Error populating database: {e}'))
>>>>>>> 2d7d7f7 (Align project structure with recommended setup and update dependencies)
