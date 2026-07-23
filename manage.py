#!/usr/bin/env python
"""Django'ning loyihani boshqarish uchun mo'ljallangan skripti.

Ushbu skript serverni ishga tushirish, migratsiyalarni bajarish va testlarni o'tkazish
kabi ma'muriy buyruqlarni bajarish uchun xizmat qiladi.
"""
import os
import sys


def main():
    """Django ma'muriy buyruqlarini ishga tushiruvchi asosiy funksiya.

    Atrof-muhit o'zgaruvchisiga 'config.settings' moduli o'rnatiladi va
    sys.argv orqali kelgan buyruqlar bajariladi.
    """
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Django yuklanmadi. U o'rnatilganiga va PYTHONPATH da mavjudligiga"
            " ishonch hosil qiling."
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
