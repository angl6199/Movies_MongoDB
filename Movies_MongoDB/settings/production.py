from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['moviesmongodb.herokuapp.com']

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
        'default': {
        'ENGINE': 'djongo',
        'NAME': 'movies',
        'HOST': 'mongodb+srv://admin:asdf@clustermovies.b4rru.mongodb.net/myFirstDatabase?retryWrites=true&w=majority',
        'USER': 'admin',
        'PASSWORD': 'asdf',
    }
}