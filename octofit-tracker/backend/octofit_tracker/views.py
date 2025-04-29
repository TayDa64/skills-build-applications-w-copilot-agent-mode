from rest_framework import viewsets
<<<<<<< HEAD
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User, Team, Activity, Leaderboard, Workout
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': request.build_absolute_uri('users/'),
        'teams': request.build_absolute_uri('teams/'),
        'activity': request.build_absolute_uri('activity/'),
        'leaderboard': request.build_absolute_uri('leaderboard/'),
        'workouts': request.build_absolute_uri('workouts/'),
    })

=======
from .models import User, Team, Activity, Leaderboard, Workout
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer

>>>>>>> 2d7d7f7 (Align project structure with recommended setup and update dependencies)
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class LeaderboardViewSet(viewsets.ModelViewSet):
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer

class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
<<<<<<< HEAD
    serializer_class = WorkoutSerializer
=======
    serializer_class = WorkoutSerializer
>>>>>>> 2d7d7f7 (Align project structure with recommended setup and update dependencies)
