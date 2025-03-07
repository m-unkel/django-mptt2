from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class MpttConfig(AppConfig):
    name = "mptt2"
    verbose_name = _("mptt2")
    default_auto_field = 'django.db.models.AutoField'
