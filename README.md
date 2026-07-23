# ⚡ Django Blog & To'liq CI/CD Pipeline Loyihasi

Ushbu loyiha **Django 5** freymvorkida yaratilgan zamonaviy blog platformasi bo'lib, unga **Docker konteynerlashtirish**, **GitHub Actions orqali avtomatik CI/CD pipeline** hamda local CD jarayonini test qilish mexanizmlari kiritilgan.

---

## 📋 Mundarija
1. [Loyiha haqida](#loyiha-haqida)
2. [Loyiha strukturasi](#loyiha-strukturasi)
3. [Local muhitda ishga tushirish (Virtualenv)](#local-muhitda-ishga-tushirish-virtualenv)
4. [Docker orqali ishga tushirish](#docker-orqali-ishga-tushirish)
5. [Unit Testlar va Kod Sifatini Tekshirish (CI)](#unit-testlar-va-kod-sifatini-tekshirish-ci)
6. [CI/CD Jarayoni Tavsifi](#cicd-jarayoni-tavsifi)
7. [Local Muhitda CD (Deployment) ni Test Qilish](#local-muhitda-cd-deployment-ni-test-qilish)

---

## 📌 Loyiha haqida

Loyiha quyidagi asosiy imkoniyatlarga ega:
- **Maqolalar ro'yxatini ko'rish (PostListView):** Sahifalangan (pagination) va responsive interfeys.
- **Maqola tafsilotlarini ko'rish (PostDetailView):** Har bir maqolaning to'liq matni va ma'lumotlari.
- **Yangi maqola yaratish (PostCreateView):** Django ModelForm yordamida maqola qo'shish va avtomatik `slug` generatsiya qilish.
- **Hujjatlashtirilgan kod:** Loyihadagi barcha model, view, form va test funksiyalari uchun batafsil Uzbek tilida `docstring`lar yozilgan.
- **To'liq CI/CD:** GitHub Actions workflow yordamida har bir push/pull request avtomatik ravishda test qilinadi va Docker obrazga yig'iladi.

---

## 📁 Loyiha strukturasi

```text
django_blog/
├── .github/
│   └── workflows/
│       └── ci-cd.yml          # GitHub Actions CI/CD pipeline fayli
├── blog/
│   ├── migrations/            # DB migratsiyalari
│   ├── admin.py               # Django Admin sozlamalari (docstring bilan)
│   ├── apps.py                # App konfiguratsiyasi (docstring bilan)
│   ├── forms.py               # PostForm va validatsiyalar (docstring bilan)
│   ├── models.py              # Post modeli (docstring bilan)
│   ├── tests.py               # Model va View unit testlari (docstring bilan)
│   ├── urls.py                # Blog yo'nalishlari
│   └── views.py               # Class-based view'lar (docstring bilan)
├── config/
│   ├── settings.py            # Asosiy sozlamalar
│   ├── urls.py                # Asosiy URL konfiguratsiyasi
│   ├── wsgi.py                # WSGI kirish nuqtasi
│   └── asgi.py                # ASGI kirish nuqtasi
├── scripts/
│   └── deploy.sh              # Local CD test skripti (hujjatlashtirilgan)
├── templates/
│   ├── base.html              # Asosiy HTML shablon (Bootstrap 5 & Glassmorphism)
│   └── blog/
│       ├── post_list.html     # Maqolalar ro'yxati
│       ├── post_detail.html   # Maqola batafsil sahifasi
│       └── post_form.html     # Yangi maqola shakli
├── .flake8                    # Flake8 linter sozlamasi
├── .gitignore                 # Git tomonidan e'tiborsiz qoldiriladigan fayllar
├── Dockerfile                 # Docker obraz konfiguratsiyasi
├── docker-compose.yml         # Local konteynerlar boshqaruvi
├── manage.py                  # Django boshqaruv skripti
├── README.md                  # Loyiha qo'llanmasi
└── requirements.txt           # Kutubxonalar ro'yxati
```

---

## 💻 Local muhitda ishga tushirish (Virtualenv)

### 1. Papkaga o'tish:
```bash
cd C:\Users\waxen\Desktop\n77\django_blog
```

### 2. Virtual muhit yaratish va faollashtirish:
```bash
# Virtual muhit yaratish
python -m venv venv

# Windows (PowerShell yoki CMD):
venv\Scripts\activate

# Linux / MacOS:
source venv/bin/activate
```

### 3. Kutubxonalarni o'rnatish:
```bash
pip install -r requirements.txt
```

### 4. Migratsiyalarni bajarish:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Superuser (Admin) yaratish (Ixtiyoriy):
```bash
python manage.py createsuperuser
```

### 6. Local serverni ishga tushirish:
```bash
python manage.py runserver
```
Saytga kirish: `http://127.0.0.1:8000/`

---

## 🐳 Docker orqali ishga tushirish

Loyiha Docker konteynerida ishlashga to'liq tayyorlangan:

```bash
# Docker Compose bilan ishga tushirish
docker-compose up --build
```
Konteyner ishga tushgach, brauzerda `http://localhost:8000/` manzilini oching.

---

## 🧪 Unit Testlar va Kod Sifatini Tekshirish (CI)

### 1. Unit testlarni yurgizish:
```bash
python manage.py test
```

### 2. Kod stilini (Flake8 linter) tekshirish:
```bash
flake8 .
```

---

## 🔄 CI/CD Jarayoni Tavsifi

Loyiha `.github/workflows/ci-cd.yml` fayli orqali **GitHub Actions** bilan avtomatlashtirilgan.

### Jarayon 2 ta asosiy bosqichdan (Job) iborat:

1. **🧪 Continuous Integration (CI):**
   - Kod GitHub'ga `push` qilinganda yoki `Pull Request` ochilganda avtomatik ishlaydi.
   - Python 3.12 muhiti o'rnatiladi.
   - `requirements.txt` kutubxonalari yuklanadi.
   - `flake8` orqali kod stili tekshiriladi.
   - `python manage.py test` buyrug'i orqali barcha unit testlar o'tkaziladi.

2. **🐳 Continuous Deployment (CD):**
   - CI bosqichi **xatosiz muvaffaqiyatli tugasa**, avtomatik ravishda CD bosqichi boshlanadi.
   - Loyihaning yangi `Dockerfile` obrazini yaratadi (Build).
   - Docker obrazini sinov tariqasida konteynerda ishga tushirib, ishlashini tasdiqlaydi.

---

## 🛠️ Local Muhitda CD (Deployment) ni Test Qilish

Server sotib olmasdan ham CD jarayonini local kompyuteringizda 2 xil usulda test qilishingiz mumkin:

### Usul 1: `scripts/deploy.sh` skripti yordamida
Loyiha ichidagi `scripts/deploy.sh` fayli local CD jarayonini avtomatlashtiradi.

```bash
# Git Bash yoki Linux terminalida:
chmod +x scripts/deploy.sh
./scripts/deploy.sh
```

**Ushbu skript ketma-ketlikda:**
1. Flake8 va Django unit testlarini o'tkazadi (Local CI).
2. Migratsiyalar va statik fayllarni toplaydi.
3. Docker obrazini build qilib, local Docker konteynerda deploy qiladi (Local CD).

### Usul 2: `act` vositasidan foydalanish (GitHub Actions'ni localda ishga tushirish)
GitHub Actions workflow'larini serverga yubormasdan localda test qilish uchun `act` dasturidan foydalanish mumkin:
1. `act` ni o'rnating: https://github.com/nektos/act
2. Terminalda buyruqni bering:
   ```
   bash
   act
   ```
U GitHub Actions workflow'ini o'z kompyuteringizdagi Docker muhitida 100% bir xil qaytarib o'tkazib beradi.





