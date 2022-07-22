from django.contrib import admin

from .models import FoodCategory, Food


@admin.register(FoodCategory)
class FoodCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_ru', 'name_en', 'name_ch', 'order_id',)
    search_fields = ('id', 'name_ru', 'name_en', 'name_ch',)
    ordering = ('id',)


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'is_vegan', 'is_special', 'code', 'internal_code', 'is_publish',)
    list_filter = ('is_vegan', 'code', 'is_publish',)
    search_fields = ('code', 'name_ru', 'category',)
    ordering = ('id',)

