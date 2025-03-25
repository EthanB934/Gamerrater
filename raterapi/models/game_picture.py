from django.db import models
class GamePicture(models.Model):
    game = models.ForeignKey("Game", on_delete=models.DO_NOTHING, related_name="pictures")
    picture = models.ImageField(
        upload_to="game_image", height_field=None,
        width_field=None, max_length=None, null=True
    )