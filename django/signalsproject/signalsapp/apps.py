from django.apps import AppConfig


class SignalsappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'signalsapp'
    
    def ready(self):
        from . import signals
