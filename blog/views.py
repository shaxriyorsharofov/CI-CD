"""Blog ilovasining ko'rinishlari (Views).

Ushbu faylda maqolalar ro'yxati, batafsil ko'rinishi va yangi maqola yaratish
uchun mo'ljallangan Class-Based View'lar joylashgan.
"""
from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import QuerySet
from django.http import HttpResponse
from django.views.generic import CreateView, DetailView, ListView

from .forms import PostForm
from .models import Post


class PostListView(ListView):
    """Chop etilgan maqolalar ro'yxatini ko'rsatuvchi ko'rinish sinfi.

    Atributlar:
        model (Post): Foydalaniladigan model.
        template_name (str): HTML shablon fayli yo'li.
        context_object_name (str): Shablonga uzatiladigan obyektlar ro'yxati nomi.
        paginate_by (int): Har bir sahifadagi maqolalar soni.
    """

    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self) -> QuerySet[Post]:
        """Faqat chop etilgan ('published') maqolalarni saralab qaytaradi.

        Returns:
            QuerySet[Post]: Chop etilgan maqolalar ro'yxati.
        """
        return Post.objects.filter(status='published').order_by('-created_at')


class PostDetailView(DetailView):
    """Alohida bir maqolaning to'liq matnini va ma'lumotlarini ko'rsatuvchi ko'rinish sinfi.

    Atributlar:
        model (Post): Foydalaniladigan model.
        template_name (str): HTML shablon fayli yo'li.
        context_object_name (str): Shablonga uzatiladigan obyekt nomi.
        slug_field (str): Slug maydoni nomi.
        slug_url_kwarg (str): URL parametrida berilgan slug kaliti nomi.
    """

    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_queryset(self) -> QuerySet[Post]:
        """Chop etilgan maqolani izlaydi.

        Returns:
            QuerySet[Post]: Tanlangan va chop etilgan maqola.
        """
        return Post.objects.filter(status='published')


class PostCreateView(CreateView):
    """Yangi maqola yaratish uchun mo'ljallangan ko'rinish sinfi.

    Atributlar:
        model (Post): Foydalaniladigan model.
        form_class (PostForm): Maqola yaratish uchun forma.
        template_name (str): HTML shablon fayli.
    """

    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def form_valid(self, form: PostForm) -> HttpResponse:
        """Forma ma'lumotlari to'g'ri to'ldirilganda ishlaydigan metod.

        Agar foydalanuvchi tizimga kirmagan bo'lsa, avtomatik ravishda birinchi
        foydalanuvchi yoki 'admin' foydalanuvchisini muallif sifatida biriktiradi.

        Args:
            form (PostForm): Tekshirilgan forma obyekti.

        Returns:
            HttpResponse: Muvaffaqiyatli saqlangandan so'ng yo'naltirish response'i.
        """
        if self.request.user.is_authenticated:
            form.instance.author = self.request.user
        else:
            # Tizimda foydalanuvchi bo'lmasa, standart muallif biriktiriladi
            default_user, _ = User.objects.get_or_create(
                username='admin',
                defaults={'email': 'admin@example.com'}
            )
            form.instance.author = default_user

        messages.success(self.request, "Yangi maqola muvaffaqiyatli yaratildi!")
        return super().form_valid(form)
