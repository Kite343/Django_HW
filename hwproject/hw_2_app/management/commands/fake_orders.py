from random import choice
from django.core.management.base import BaseCommand
from hw_2_app.models import *

class Command(BaseCommand):
    help = "Generate fake orders."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        products = Product.objects.all()

        for client in Client.objects.all():
            order = Order.objects.create(client=client)
            sum_price = 0
            for _ in range(count):
                product = choice(products)
                order.product.add(product)
                sum_price += product.price
            order.total_amount = sum_price
            order.save()

# python manage.py fake_orders _number_
