from django.db import models
from django.contrib.auth.models import User

class Game(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Game")
    title = models.CharField(max_length=100)
    description = models.TextField()
    designer = models.CharField(max_length=100)
    year_released = models.IntegerField()
    player_count = models.IntegerField()
    play_time = models.IntegerField()
    age_to_play = models.IntegerField()
    categories = models.ManyToManyField("Category", through="GameCategory", related_name="Game")
