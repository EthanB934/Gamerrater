from rest_framework import serializers, viewsets,status
from rest_framework.response import Response
from raterapi.models import Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name",)

class CategoryViewSet(viewsets.ViewSet):
    def list(self, request):
        try:
            categories = Category.objects.all()
            serializer = CategorySerializer(categories, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as ex:
            return Response(ex, status=status.HTTP_404_NOT_FOUND)
