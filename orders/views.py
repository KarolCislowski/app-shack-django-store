from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Order
from .serializers import OrderSerializer, MyOrderSerializer


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def checkout(request):
    serializer = OrderSerializer(data=request.data)

    if serializer.is_valid():
        total_value = sum(item.get(
            'quantity') * item.get('product').price for item in serializer.validated_data['items'])
        try:
            serializer.save(costumer=request.user, total_value=total_value)

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrdersList(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        orders = Order.objects.filter(costumer=request.user)
        serializer = MyOrderSerializer(orders, many=True)
        return Response(serializer.data)
