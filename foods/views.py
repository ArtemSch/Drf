from rest_framework import generics
from rest_framework.permissions import AllowAny

from .models import Food
from .serializers import FoodListSerializer


class FoodsListAPIView(generics.ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = FoodListSerializer
    queryset = Food.objects.filter(is_publish=True)
