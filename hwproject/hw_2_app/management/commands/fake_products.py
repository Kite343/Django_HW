from random import choice
from django.core.management.base import BaseCommand
from hw_2_app.models import *

class Command(BaseCommand):
    help = "Generate fake products."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        products = ['milk', 'Kryptonite', 'rom', 'lemonade', 'fish', 'meat', 'bread', 'cheese', 'honey', 'banana']        
        for i in range(1, count + 1):
            product = Product(name=f'{choice(products)}_{i}', description='text',
                               price=i*3.5, quantity=i*15, )
            product.save()

# python manage.py fake_products _number_