from django.apps import AppConfig


class GalleriesConfig(AppConfig):
    name = 'shinywaffle.galleries'
    verbose_name = "Galleries"

    def ready(self):
        """Override this to put in:
            Users system checks
            Users signal registration
        """
        pass
