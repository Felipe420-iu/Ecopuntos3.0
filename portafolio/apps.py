from django.apps import AppConfig


class PortafolioConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'portafolio'
    verbose_name = 'Portafolio'
    
    class meta:
        verbose_name = 'Portafolio'
        verbose_name_plural = 'Portafolios'
        ordering = ['-created_at']
    def __str__(self):
        return self.title