"""
dj-stripe - Django + Stripe Made Easy
"""
from django.apps import AppConfig
from importlib.metadata import version

__version__ = version("dj-stripe")

default_app_config = "djstripe.DjstripeAppConfig"


class DjstripeAppConfig(AppConfig):
    """
    An AppConfig for dj-stripe which loads system checks
    and event handlers once Django is ready.
    """

    name = "djstripe"

    def ready(self):
        import stripe
        from . import (  # noqa: Register the checks and event handlers
            checks,
            event_handlers,
        )

        # Set app info
        # https://stripe.com/docs/building-plugins#setappinfo
        stripe.set_app_info(
            "dj-stripe",
            version=__version__,
            url="https://github.com/dj-stripe/dj-stripe",
        )
