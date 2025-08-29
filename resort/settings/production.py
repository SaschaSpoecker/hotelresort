import environ
import os
from .base import *

DEBUG = False

try:
    from .local import *
except ImportError:
    pass


env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

SECRET_KEY = env('SECRET_KEY')

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['*'])

DATABASES = {
    'default': env.db(),
}
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

MEDIA_ROOT = env('MEDIA_ROOT', default=os.path.join(BASE_DIR, 'media'))  
MEDIA_URL = env('MEDIA_URL', default='/media/')
