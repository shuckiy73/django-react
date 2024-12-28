from django.contrib import admin
from .models import User, Post

# Регистрация модели User
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone', 'is_staff')  # Поля, отображаемые в списке
    search_fields = ('username', 'email', 'phone')  # Поля для поиска
    list_filter = ('is_staff', 'is_superuser')  # Фильтры

# Регистрация модели Post
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at')  # Поля, отображаемые в списке
    search_fields = ('title', 'content')  # Поля для поиска
    list_filter = ('created_at', 'updated_at')  # Фильтры
    date_hierarchy = 'created_at'  # Иерархия по дате