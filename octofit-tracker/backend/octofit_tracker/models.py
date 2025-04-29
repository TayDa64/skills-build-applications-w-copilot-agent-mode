from djongo import models

class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
<<<<<<< HEAD
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=255)
    members = models.ArrayField(model_container=User)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=255)
    duration = models.IntegerField()  # in minutes
    date = models.DateField()

    def __str__(self):
        return f"{self.activity_type} by {self.user.name}"
=======
    # Add other fields as needed

class Team(models.Model):
    name = models.CharField(max_length=255)
    members = models.ManyToManyField(User)

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    date = models.DateTimeField()
>>>>>>> 2d7d7f7 (Align project structure with recommended setup and update dependencies)

class Leaderboard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()

<<<<<<< HEAD
    def __str__(self):
        return f"{self.user.name}: {self.score}"

class Workout(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.IntegerField()  # in minutes

    def __str__(self):
        return self.name
=======
class Workout(models.Model):
    name = models.CharField(max_length=255)
    duration = models.IntegerField()
>>>>>>> 2d7d7f7 (Align project structure with recommended setup and update dependencies)
