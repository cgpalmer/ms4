from django.apps import AppConfig


# This code has been copied directly from Boutique Ado - Code Institute
class CheckoutConfig(AppConfig):
    name = 'checkout'

    def ready(self):
        import checkout.signals
