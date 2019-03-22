from django.apps import AppConfig
import django_heroku


class T1Config(AppConfig):
    name = 't1'


django_heroku.settings(locals())
