"""Blog ilovasi uchun avtomatlashtirilgan unit testlar.

Ushbu fayl model mantiqlari, view ish faoliyati va URL manzillarining
to'g'ri ishlashini avtomatik tekshirish uchun testlarni o'z ichiga oladi.
CI/CD jarayonida ushbu testlar avtomatik ishga tushadi.
"""
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Post


class BlogModelAndViewsTestCase(TestCase):
    """Blog modeli va ko'rinishlarini sinovdan o'tkazuvchi test sinfi."""

    def setUp(self) -> None:
        """Testlar ishga tushishidan oldin dastlabki ma'lumotlarni tayyorlash."""
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword123'
        )
        self.post = Post.objects.create(
            title='Test Maqola Sarlavhasi',
            content='Test maqolasining to\'liq mazmuni va matni.',
            author=self.user,
            status='published'
        )

    def test_post_creation(self) -> None:
        """Post modelida maqola to'g'ri saqlanishi va slug avto-generatsiyasini tekshiradi."""
        self.assertEqual(self.post.title, 'Test Maqola Sarlavhasi1')
        self.assertEqual(self.post.slug, 'test-maqola-sarlavhasi')
        self.assertEqual(str(self.post), 'Test Maqola Sarlavhasi')
        self.assertEqual(self.post.status, 'published')

    def test_post_list_view(self) -> None:
        """Maqolalar ro'yxati sahifasi (post_list) HTTP 200 status qaytarishini va kontentni tekshiradi."""
        url = reverse('blog:post_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Maqola Sarlavhasi')
        self.assertTemplateUsed(response, 'blog/post_list.html')

    def test_post_detail_view(self) -> None:
        """Alohida maqola ko'rish sahifasi (post_detail) to'g'ri ishlashini tekshiradi."""
        url = reverse('blog:post_detail', kwargs={'slug': self.post.slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test maqolasining')
        self.assertContains(response, 'mazmuni va matni.')
        self.assertTemplateUsed(response, 'blog/post_detail.html')

    def test_post_create_view(self) -> None:
        """Yangi maqola yaratish formasining ish faoliyatini va ma'lumot bazasiga saqlanishini tekshiradi."""
        url = reverse('blog:post_create')
        data = {
            'title': 'Yangi Yaratilgan Post',
            'content': 'Forma orqali yaratilgan maqola matni.',
            'status': 'published'
        }
        response = self.client.post(url, data)
        # Yaratilgach, maqola sahifasiga yo'naltiradi (302 Redirect)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Post.objects.filter(title='Yangi Yaratilgan Post').exists())
