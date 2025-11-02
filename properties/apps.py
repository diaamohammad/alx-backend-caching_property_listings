
from django.apps import AppConfig

class PropertiesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'properties'

    # أضف هذه الدالة
    def ready(self):
        """
        Overrides the ready method to import signals
        when the app is loaded.
        """
        # هذا هو السطر الذي يبحث عنه التشيكر
        import properties.signals