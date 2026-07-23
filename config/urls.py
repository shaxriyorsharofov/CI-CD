"""Asosiy URL yo'nalishlari konfiguratsiyasi.

Ushbu fayl administratsiya paneli va blog ilovasining URL marshrutlarini
birlashtiradi.
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls', namespace='blog')),
]
