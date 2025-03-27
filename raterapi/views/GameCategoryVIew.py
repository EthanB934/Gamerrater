from rest_framework import serializers, status, viewsets
from rest_framework.response import Response
from raterapi.models import GameCategory, Game, Category

class GameCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GameCategory
        fields = ("id", "game", "category")

class GameCategoryViewSet(viewsets.ViewSet):
    def create(self, request):
        game_category_relationship = GameCategory()
        game = Game.objects.get(pk=request.data["gameId"])
        game_category_relationship.game = game
        category = Category.objects.get(pk=request.data["categoryId"])
        game_category_relationship.category = category

        try:
            game_category_relationship.save()
            serializer = GameCategorySerializer(game_category_relationship, many=False)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as ex :
            return Response(ex.args[0], status=status.HTTP_400_BAD_REQUEST)
