from django.apps import AppConfig
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

from mongoengine import connection

class DjangoMongoManiacConfig(AppConfig):
    name = 'django_mongomaniac'
    verbose_name = "Django-MongoManiac"

    if not hasattr(settings, 'MONGODB_DATABASES'):
        raise ImproperlyConfigured("Missing 'MONGODB_DATABASES' in settings.py")

    if not settings.MONGODB_DATABASES.get('test'):
        raise ImproperlyConfigured("Missing 'test' database configuration in 'MONGODB_DATABASES'")

    try:
        connection.DEFAULT_CONNECTION_NAME = 'test'
        connection.register_connection(alias='test', **settings.MONGODB_DATABASES.get('test'))
    except Exception as e:
        raise ImproperlyConfigured("Improperly 'test' database configuration in 'MONGODB_DATABASES': " + str(e))