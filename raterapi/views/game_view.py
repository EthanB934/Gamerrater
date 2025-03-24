from rest_framework import serializers, viewsets, status
from rest_framework.response import Response
from raterapi.models import Game

class GameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Game
        fields = ("id", "user", "title", "picture_of_game", "description", "designer", "year_released", "player_count", "play_time", "age_to_play")
        
class GameViewSet(viewsets.ViewSet):
    def list(self, request):
        games = Game.objects.all()
        serializer = GameSerializer(games, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        game = Game.objects.get(pk=pk)
        serializer = GameSerializer(game, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        game = Game()
        game.user = request.auth.user
        game.title = request.data["title"]
        game.picture_of_game = request.data["image"]
        game.description = request.data["description"]
        game.designer = request.data["designer"]
        game.year_released = request.data["year"]
        game.player_count = request.data["players"]
        game.play_time = request.data["play_time"]
        game.age_to_play = request.data["age_to_play"]

        try: 
            game.save()
            serializer = GameSerializer(game, many=False)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as ex:
            return Response(ex.args[0], status=status.HTTP_400_BAD_REQUEST)