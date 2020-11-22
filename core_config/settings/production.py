"""Production envs."""

import dj_database_url
from decouple import Csv, AutoConfig

from .common import *

config = AutoConfig(search_path=BASE_DIR / '/envs_vars/.env.prod')

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

# AWS_ACCESS_KEY_ID = config('SPACES_ACCESS_KEY')
# AWS_SECRET_ACCESS_KEY = config('SPACES_SECRET_ACCESS_KEY')
# AWS_STORAGE_BUCKET_NAME = ''
# AWS_S3_ENDPOINT_URL = 'https://nyc3.digitaloceanspaces.com'
# AWS_S3_OBJECT_PARAMETERS = {
#   'CacheControl': 'max-age=86400',
# }
# AWS_LOCATION = ''
