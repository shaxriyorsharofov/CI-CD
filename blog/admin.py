"""Django administratsiya paneli uchun sozlamalar.

Post modelini administratsiya panelida qulay boshqarish uchun moslashtirish.
"""
from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Post modelini admin panelida ko'rsatish sozlamalari sinfi.

    Atributlar:
        list_display (tuple): Admin ro'yxatida ko'rinadigan ustunlar.
        list_filter (tuple): Yon paneldagi filterlar.
        search_fields (tuple): Qidiruv bo'yicha ustunlar.
        prepopulated_fields (dict): Sarlavhaga qarab slug'ni avto to'ldirish.
    """

    list_display = ('title', 'slug', 'author', 'status', 'created_at')
    list_filter = ('status', 'created_at', 'author')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created_at'
    ordering = ('status', '-created_at')
