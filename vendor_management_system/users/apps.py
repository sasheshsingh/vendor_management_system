import contextlib

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "vendor_management_system.users"
    verbose_name = _("Users")

    def ready(self):
        with contextlib.suppress(ImportError):
            import vendor_management_system.users.signals  # noqa: F401
