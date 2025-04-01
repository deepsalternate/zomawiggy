from django.apps import AppConfig
# from .signals import create_profile_receiver

class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'
    #
    def ready(self):
        import accounts.signals

