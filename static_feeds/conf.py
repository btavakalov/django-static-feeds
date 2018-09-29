from django.conf import settings

# Path to root location where the feeds will be stored.
ROOT_DIR = getattr(settings, 'STATICFEEDS_ROOT_DIR', settings.STATIC_ROOT)

# Storage class to use.
STORAGE_CLASS = getattr(settings, 'STATICFEEDS_STORAGE', 'django.core.files.storage.FileSystemStorage')

FEEDS_URLS = settings.STATICFEEDS_URLS

# How often should the celery task be run.
CELERY_TASK_REPETITION = getattr(settings, 'STATICFEEDS_REFRESH_AFTER', 5)
