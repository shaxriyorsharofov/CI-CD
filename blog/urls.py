"""Blog ilovasi uchun URL marshruti konfiguratsiyasi.

Ushbu fayl maqolalar ro'yxati, batafsil sahifa va yangi maqola yaratish
sahifalarining URL yo'nalishlarini belgilaydi.
"""
from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('post/new/', views.PostCreateView.as_view(), name='post_create'),
    path('post/<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
]
