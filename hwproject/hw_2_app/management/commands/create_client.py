from django.core.management.base import BaseCommand
from hw_2_app.models import *

class Command(BaseCommand):
    help = "Create client."

    def handle(self, *args, **kwargs):
        client = Client(name='John', email='john@example.com',
                    phone = '+7777667788', address = "1 street")
        client.save()
        self.stdout.write(f'{client}')

# python manage.py create_client