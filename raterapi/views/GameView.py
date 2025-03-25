from rest_framework import serializers, viewsets, status
from rest_framework.response import Response
from raterapi.models import Game
from raterapi.views.CategoryView import CategorySerializer

class GameSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)

    class Meta:
        model = Game
        fields = ("id", "title", "description", "designer", "year_released", "player_count", "play_time", "age_to_play", "categories")

class GameViewSet(viewsets.ViewSet):
    def list(self, request):
        try:
            games = Game.objects.all()  
            serializer = GameSerializer(games, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as ex:
            return Response(f'{ex.args[0]}', status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def retrieve(self, request, pk=None):
        try:
            game = Game.objects.get(pk=pk)
            serializer = GameSerializer(game, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as ex:
            return Response(f'{ex.args[0]}', status=status.HTTP_404_NOT_FOUND)
