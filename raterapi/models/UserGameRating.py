from django.db import models
from django.contrib.auth.models import User

class UserGameRating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserGameRating")
    game = models.ForeignKey("Game", on_delete=models.CASCADE, related_name="UserGameRating")
    rating = models.IntegerField()