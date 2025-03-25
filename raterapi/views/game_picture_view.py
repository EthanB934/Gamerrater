import uuid
import base64
from django.core.files.base import ContentFile
from rest_framework import serializers, viewsets, status
from rest_framework.response import Response
from raterapi.models import GamePicture, Game

class GamePictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = GamePicture
        fields = ("id","game", "picture",)

class GamePictureViewSet(viewsets.ViewSet):
    def create(self, request):
        game_picture = GamePicture()
        game = Game.objects.get(pk=request.data["game"])
        game_picture.game = game

        format, imgstr = request.data["game_image"].split(";base64,")
        ext = format.split("/")[-1]
        data = ContentFile(base64.b64decode(imgstr), name=f'{request.data["game"]} - {uuid.uuid4()}.{ext}')

        game_picture.picture = data
        
        try:
            game_picture.save()
            serializer = GamePictureSerializer(game_picture, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as ex:
            return Response(ex.args[0], status=status.HTTP_400_BAD_REQUEST)