import os
from pathlib import Path
import dj_database_url
from dotenv import load_dotenv
from django.urls import reverse_lazy

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

UNFOLD = {
    "SITE_TITLE": "DSST Admin",
    "SITE_HEADER": "DSST School Management",
    "SITE_URL": "/",
    "SITE_ICON": None,
    "SITE_SYMBOL": "school",
    "SHOW_HISTORY": True,
    "SHOW_VIEW_ON_SITE": True,
    "COLORS": {
        "primary": {
            "50": "240 249 255",
            "100": "224 242 254",
            "200": "186 230 253",
            "300": "125 211 252",
            "400": "56 189 248",
            "500": "14 165 233",
            "600": "2 132 199",
            "700": "3 105 161",
            "800": "7 89 133",
            "900": "12 74 110",
            "950": "8 47 73",
        },
    },
    "SIDEBAR": {
        "show_search": True,
        "show_all_applications": True,
        "navigation": [
            {
                "title": "Navigation",
                "items": [
                    {
                        "title": "Dashboard",
                        "icon": "dashboard",
                        "link": reverse_lazy("admin:index"),
                    },
                ],
            },
            {
                "title": "Content",
                "collapsible": True,
                "items": [
                    {"title": "Notice Board", "icon": "newspaper", "link": reverse_lazy("admin:main_post_changelist")},
                    {"title": "Marquee Items", "icon": "campaign", "link": reverse_lazy("admin:main_marqueeitem_changelist")},
                    {"title": "Gallery", "icon": "photo_library", "link": reverse_lazy("admin:main_galleryimage_changelist")},
                    {"title": "Achievements", "icon": "emoji_events", "link": reverse_lazy("admin:main_achievement_changelist")},
                ],
            },
            {
                "title": "School",
                "collapsible": True,
                "items": [
                    {"title": "Teachers", "icon": "school", "link": reverse_lazy("admin:main_teacher_changelist")},
                    {"title": "Departments", "icon": "category", "link": reverse_lazy("admin:main_department_changelist")},
                    {"title": "Labs & Facilities", "icon": "science", "link": reverse_lazy("admin:main_lab_changelist")},
                ],
            },
            {
                "title": "Students",
                "collapsible": True,
                "items": [
                    {"title": "Admissions", "icon": "how_to_reg", "link": reverse_lazy("admin:main_admissionapplication_changelist")},
                    {"title": "Fee Payments", "icon": "payments", "link": reverse_lazy("admin:main_feepayment_changelist")},
                    {"title": "Contact Messages", "icon": "mail", "link": reverse_lazy("admin:main_contactmessage_changelist")},
                ],
            },
        ],
    },
}

# SECURITY
SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = os.getenv('DEBUG', 'False') == 'True'

ALLOWED_HOSTS = [
    'dsstwebsite.onrender.com',
    'www.dsstwebsite.onrender.com',
    'localhost',
    '127.0.0.1',
]

CSRF_TRUSTED_ORIGINS = [
    'https://dsstwebsite.onrender.com',
    'https://www.dsstwebsite.onrender.com',
]

# APPLICATIONS
INSTALLED_APPS = [
    "unfold",
    "unfold.contrib.filters",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cloudinary',
    'cloudinary_storage',
    'main',
]

# MIDDLEWARE
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'school_website.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'school_website.wsgi.application'

# DATABASE
DATABASES = {
    'default': dj_database_url.parse(
        os.getenv('DATABASE_URL'),
        conn_max_age=600,
        ssl_require=True,
    )
}

# CLOUDINARY
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.getenv("CLOUDINARY_CLOUD_NAME"),
    'API_KEY': os.getenv("CLOUDINARY_API_KEY"),
    'API_SECRET': os.getenv("CLOUDINARY_API_SECRET"),
    'RESOURCE_TYPES': ['image', 'video', 'raw'],
}
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# PASSWORD VALIDATORS
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# INTERNATIONALIZATION
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_TZ = True

# STATIC FILES
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# MEDIA
MEDIA_URL = '/media/'

# COOKIES & SESSION — fixes mobile 404/CSRF issues
SESSION_COOKIE_SAMESITE = 'Lax'
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SAMESITE = 'Lax'
CSRF_COOKIE_SECURE = True
APPEND_SLASH = True

# SECURITY HEADERS
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'SAMEORIGIN'
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# AUTH
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'