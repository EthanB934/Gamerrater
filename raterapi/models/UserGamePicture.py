from django.db import models
from django.contrib.auth.models import User

class UserGamePicture(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserGamePicture")
    game = models.ForeignKey("Game", on_delete=models.CASCADE, related_name="UserGamePicture")
    picture = models.ImageField(upload_to="gamepictures", height_field=None, width_field=None, max_length=None, null=True)