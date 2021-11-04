from django.apps import AppConfig


class FvirtualConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Fvirtual'

    def ready(self):
        import Fvirtual.signals

 