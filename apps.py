from django.apps import AppConfig


class CustomersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'customer'
    verbose_name = 'Customer Management'

    def ready(self):
        """
        Called when Django starts.
        """
        pass
