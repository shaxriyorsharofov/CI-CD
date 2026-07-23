"""Blog ilovasi formalar moduli.

Yangi maqola yaratish va tahrirlash uchun Django ModelForm formasi.
"""
from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    """Maqola yaratish va tahrirlash uchun forma sinfi."""

    class Meta:
        model = Post
        fields = ['title', 'content', 'status']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Maqola sarlavhasini kiriting...'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 6,
                'placeholder': 'Maqola matnini batafsil yozing...'
            }),
            'status': forms.Select(attrs={
                'class': 'form-select'
            }),
        }

    def clean_title(self) -> str:
        """Sarlavha maydonini validsiyadan o'tkazish funksiyasi.

        Returns:
            str: Tozalangan va tekshirilgan sarlavha.

        Raises:
            forms.ValidationError: Agar sarlavha 3 tadan kam belgilardan iborat bo'lsa.
        """
        title = self.cleaned_data.get('title', '')
        if len(title.strip()) < 3:
            raise forms.ValidationError(
                "Sarlavha kamida 3 ta belgidan iborat bo'lishi kerak!"
            )
        return title
