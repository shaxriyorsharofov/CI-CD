# 1. Asosiy Python obrazini tanlaymiz (yengil va xavfsiz slim versiya)
FROM python:3.12-slim

# Python kodi uchun buferlashni o'chiramiz va .pyc fayllar yaratilishini oldini olamiz
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Ishchi katalogini belgilaymiz
WORKDIR /app

# Tizim paketlarini yangilaymiz va zarur vositalarni o'rnatamiz
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Zarur kutubxona faylini nusxalaymiz va o'rnatamiz
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Loyihaning qolgan barcha fayllarini nusxalaymiz
COPY . /app/

# Statik fayllarni toplaymiz va migratsiyalarni tayyorlaymiz
RUN python manage.py collectstatic --noinput || true

# Portni ochamiz
EXPOSE 8000

# Serverni Gunicorn orqali ishga tushiramiz
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "config.wsgi:application"]
