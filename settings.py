# esporte_sem_fronteiras/settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Use 'postgresql' para PostgreSQL
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
