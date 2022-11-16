from django.apps import AppConfig


class DataConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'data'

    def ready(self):
        print("sending data...")
        from .data_scheduler import updater
        updater.start()

