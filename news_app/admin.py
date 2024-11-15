from django.contrib import admin
from news_app.models import NewsCategory, News
# Register your models here.
@admin.register(NewsCategory)
class CategoryAdminModel(admin.ModelAdmin):
    search_fields = ["name_category", "created_at"]
    list_filter = ["created_at"]
    list_display = ["id", "name_category", "created_at"]
    ordering = ["-id"]

@admin.register(News)
class NewsAdminModel(admin.ModelAdmin):
    search_fields = ["head", "created_at"]
    list_filter = ["created_at"]
    list_display = ["id", "head", "new_cat", "created_at"]
    ordering = ["-id"]