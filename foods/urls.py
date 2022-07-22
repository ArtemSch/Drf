from django.urls import path

from .views import FoodsListAPIView

app_name = 'foods'

urlpatterns = [
    path('', FoodsListAPIView.as_view(), name='food_list'),
]
