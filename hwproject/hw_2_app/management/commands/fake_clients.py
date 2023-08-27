from random import choice
from django.core.management.base import BaseCommand
from hw_2_app.models import *

class Command(BaseCommand):
    help = "Generate fake client."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        names = ['Aleks', 'Barry Allen', 'Aquaman', 'Ray Palmer', 'John Constantine', 'Batman', 'Tony Stark', ]        
        for i in range(1, count + 1):
            client = Client(name=choice(names), email=f'{i}_mail@example.com',
                    phone = '+7777667788', address = f"{i} street")
            client.save()

# python manage.py fake_clients _number_