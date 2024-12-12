import os

# Define the base directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'myapp/static'),
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')