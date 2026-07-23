"""Blog ilovasining konfiguratsiya fayli.

Ushbu fayl Django tizimiga ilova nomi va sozlamalarini bildiradi.
"""
from django.apps import AppConfig


class BlogConfig(AppConfig):
    """Blog ilovasini sozlash sinfi."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
    verbose_name = 'Blog Boshqaruvi'
