from rest_framework import status, serializers, viewsets
from rest_framework.response import Response
from raterapi.models import UserGameReview, Game

class UserGameReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserGameReview
        fields = ("id", "user", "game", "review",)

class UserGameReviewViewSet(viewsets.ViewSet):
    def create(self, request):
        review = UserGameReview()
        review.user = request.auth.user
        game = Game.objects.get(pk=request.data["gameId"])
        review.game = game
        review.review = request.data["review"]

        try: 
            review.save()
            serializer = UserGameReviewSerializer(review, many=False)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as ex:
            return Response(ex.args[0], status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        reviews = UserGameReview.objects.all()
        serializer = UserGameReviewSerializer(reviews, many=True, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)
