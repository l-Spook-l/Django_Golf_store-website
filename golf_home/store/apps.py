from django.apps import AppConfig


class StoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'store'
    """
    Если надо меняеть значение нашего приложения в админке,
    сработает только, если в настройке приложение подключено та - 'store.apps.StoreConfig',
    """
    verbose_name = 'Магазин'
