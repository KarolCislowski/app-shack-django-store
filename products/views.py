from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .serializers import *
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import api_view, permission_classes


class CategoryView(ModelViewSet):
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]
    queryset = Category.objects.all()


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_get_categories(query):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)
