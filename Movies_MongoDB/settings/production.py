from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['moviesmongodb.herokuapp.com']

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': "finalp",
    }
}
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'movies',
        'CLIENT': {
           'host': 'mongodb+srv://admin:asdf@clustermovies.b4rru.mongodb.net/myFirstDatabase?retryWrites=true&w=majority',
        }
    }
}

STATICFILES_DIRS = (BASE_DIR, 'static')
