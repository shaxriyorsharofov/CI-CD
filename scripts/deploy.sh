#!/bin/bash
# ==============================================================================
# Local CD (Continuous Deployment) Test va Avtomatik Joylashtirish Skripti
# ==============================================================================
# Ushbu skript local kompyuterda yoki serverda CD jarayonini qo'lda yoki
# avtomatlashtirilgan tarzda sinab ko'rish uchun mo'ljallangan.
# ==============================================================================

set -e # Xatolik yuz bersa skriptni darhol to'xtatish

echo "--------------------------------------------------------"
echo "🚀 LOCAL CD (DEPLOYMENT) TEST JARAYONI BOSHLANDI"
echo "--------------------------------------------------------"

# 1-FUNKSIYA: Kod uslubi va testlarni tekshirish (Local CI)
check_quality() {
    echo "🔍 1-Qadam: Kod sifatini va unit testlarni tekshirish..."
    if command -v flake8 &> /dev/null; then
        flake8 .
        echo "✅ Flake8 linting muvaffaqiyatli o'tdi."
    else
        echo "⚠️ Flake8 topilmadi, o'tkazib yuborilmoqda..."
    fi

    python manage.py test
    echo "✅ Barcha unit testlar omadli o'tdi!"
}

# 2-FUNKSIYA: Migratsiya va statik fayllarni tayyorlash
prepare_assets() {
    echo "⚙️ 2-Qadam: Ma'lumotlar bazasi va statik fayllarni yangilash..."
    python manage.py makemigrations --noinput
    python manage.py migrate --noinput
    python manage.py collectstatic --noinput
    echo "✅ Bazalar va statik fayllar tayyorlandi."
}

# 3-FUNKSIYA: Docker obrazini yaratish va qayta ishga tushirish (Local CD)
deploy_docker() {
    echo "🐳 3-Qadam: Docker konteynerini yaratish va deploy qilish..."
    if command -v docker &> /dev/null; then
        echo "🔨 Docker build qilinmoqda..."
        docker build -t django_blog_app:latest .
        
        echo "🔄 Eski konteyner to'xtatib tozalanmoqda..."
        docker stop django_blog_container 2>/dev/null || true
        docker rm django_blog_container 2>/dev/null || true

        echo "▶️ Yangi konteyner ishga tushirilmoqda..."
        docker run -d --name django_blog_container -p 8000:8000 django_blog_app:latest
        echo "✅ Local CD Muvaffaqiyatli bajarildi! Sayt http://localhost:8000 manzilda ishlayapti."
    else
        echo "⚠️ Docker topilmadi! Standart Python serveri orqali ishga tushirilishi mumkin."
    fi
}

# Asosiy chaqiruvlar
check_quality
prepare_assets
deploy_docker

echo "--------------------------------------------------------"
echo "🎉 CD JARAYONI TUGADI! Loyiha foydalanishga tayyor."
echo "--------------------------------------------------------"
