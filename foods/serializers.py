from rest_framework import serializers

from .models import (Food, )


class FoodListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ('id', 'category', 'is_vegan', 'is_special', 'code', 'internal_code', 'name_ru', 'description_ru',
                  'description_en', 'description_ch', 'cost', 'is_publish', 'additional',)
        read_only_fields = fields
