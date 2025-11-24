import os
from pathlib import Path
from dotenv import load_dotenv
import dj_database_url   # <-- needed for Railway PostgreSQL

# ---------------------------------------------------------
# BASE DIR
# ---------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# Load environment variables from .env (local only)
if os.environ.get("RAILWAY_ENV") != "production":
    load_dotenv(BASE_DIR / ".env")

# ---------------------------------------------------------
# BASIC SECURITY
# ---------------------------------------------------------
SECRET_KEY = os.getenv("SECRET_KEY", "dev-key-change-this")
DEBUG = os.getenv("DEBUG", "True") == "True"

ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
    "stiwdiodyfi.com",
    "www.stiwdiodyfi.com",
    ".railway.app",
]

CSRF_TRUSTED_ORIGINS = [
    "https://stiwdiodyfi.com",
    "https://www.stiwdiodyfi.com",
    "https://*.railway.app",
]

# ---------------------------------------------------------
# INSTALLED APPS
# ---------------------------------------------------------
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Cloudinary
    "cloudinary",
    "cloudinary_storage",

    # Main app
    "siteapp",
]

# ---------------------------------------------------------
# MIDDLEWARE
# ---------------------------------------------------------
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "stiwdiodyfi.urls"

# ---------------------------------------------------------
# TEMPLATES
# ---------------------------------------------------------
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "stiwdiodyfi.wsgi.application"

# ---------------------------------------------------------
# DATABASE (POSTGRES on Railway, SQLITE locally)
# ---------------------------------------------------------
DATABASE_URL = os.getenv("DATABASE_URL")

if DATABASE_URL:
    DATABASES = {
        "default": dj_database_url.parse(
            DATABASE_URL,
            conn_max_age=600,
            ssl_require=True
        )
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

# ---------------------------------------------------------
# STATIC FILES
# ---------------------------------------------------------
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

# ---------------------------------------------------------
# MEDIA — CLOUDINARY
# ---------------------------------------------------------
CLOUDINARY_STORAGE = {
    "CLOUD_NAME": os.getenv("CLOUDINARY_CLOUD_NAME"),
    "API_KEY": os.getenv("CLOUDINARY_API_KEY"),
    "API_SECRET": os.getenv("CLOUDINARY_API_SECRET"),
}

DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"

MEDIA_URL = "/media/"

# ---------------------------------------------------------
# AUTO FIELD
# ---------------------------------------------------------
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
