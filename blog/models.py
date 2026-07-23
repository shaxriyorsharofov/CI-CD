"""Blog ilovasi uchun ma'lumotlar modellari (Models).

Ushbu fayl blog maqolalari va ularning xususiyatlarini saqlash uchun
mo'ljallangan `Post` modelini o'z ichiga oladi.
"""
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Post(models.Model):
    """Blog maqolasi modeli.

    Maydonlar:
        title (CharField): Maqolaning sarlavhasi.
        slug (SlugField): Maqolaning URL manzili uchun takrorlanmas slug.
        author (ForeignKey): Maqola muallifi (User modeliga bog'langan).
        content (TextField): Maqolaning to'liq matni.
        created_at (DateTimeField): Maqola yaratilgan vaqt (avtomatik).
        updated_at (DateTimeField): Maqola oxirgi marta tahrirlangan vaqt.
        status (CharField): Maqola holati ('draft' - qoralama, 'published' - chop etilgan).
    """

    STATUS_CHOICES = (
        ('draft', 'Qoralama'),
        ('published', 'Chop etilgan'),
    )

    title = models.CharField(
        max_length=250,
        verbose_name="Sarlavha",
        help_text="Maqola sarlavhasini kiriting"
    )
    slug = models.SlugField(
        max_length=250,
        unique=True,
        blank=True,
        verbose_name="Slug (URL kaliti)"
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='blog_posts',
        verbose_name="Muallif"
    )
    content = models.TextField(
        verbose_name="Maqola matni"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Yaratilgan vaqti"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Yangilangan vaqti"
    )
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='published',
        verbose_name="Holati"
    )

    class Meta:
        """Model uchun qo'shimcha meta sozlamalar."""
        ordering = ['-created_at']
        verbose_name = "Maqola"
        verbose_name_plural = "Maqolalar"

    def __str__(self) -> str:
        """Maqolaning matnli ko'rinishini qaytaradi.

        Returns:
            str: Maqola sarlavhasi.
        """
        return self.title

    def get_absolute_url(self) -> str:
        """Maqolaning batafsil ko'rish URL manzilini qaytaradi.

        Returns:
            str: 'blog:post_detail' yo'nalishining URL manzili.
        """
        return reverse('blog:post_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs) -> None:
        """Maqolani ma'lumotlar bazasiga saqlash metodi.

        Agar slug maydoni bo'sh bo'lsa, sarlavhadan kelib chiqib avtomatik
        slug generatsiya qiladi.
        """
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)





