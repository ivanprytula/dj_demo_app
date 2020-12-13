"""Production envs."""
from pathlib import Path

import dj_database_url
from decouple import Csv, AutoConfig

BASE_DIR = Path(__file__).resolve().parent.parent.parent

config = AutoConfig(search_path=BASE_DIR / 'deploy/prod/.env')

SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)
TEMPLATE_DEBUG = DEBUG
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())

DATABASES = {
    'default': config(
        'DATABASE_URL',
        cast=dj_database_url.parse
    )
}

STATIC_ROOT = BASE_DIR / 'vol/web/static'

# AWS_ACCESS_KEY_ID = config('SPACES_ACCESS_KEY')
# AWS_SECRET_ACCESS_KEY = config('SPACES_SECRET_ACCESS_KEY')
# AWS_STORAGE_BUCKET_NAME = ''
# AWS_S3_ENDPOINT_URL = 'https://nyc3.digitaloceanspaces.com'
# AWS_S3_OBJECT_PARAMETERS = {
#   'CacheControl': 'max-age=86400',
# }
# AWS_LOCATION = ''
