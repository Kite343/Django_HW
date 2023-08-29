from django.core.management.base import BaseCommand
from hw_2_app.models import *

class Command(BaseCommand):
    help = "Get all posts by author id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Product ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        product = Product.objects.filter(pk=pk).first()
        orders = Order.objects.filter(product__pk=pk)
        intro = f'All orders by {product}\n'
        text = '\n'.join(f"{order.client}" for order in orders)
        
        self.stdout.write(f'{intro} {text}')
        # self.stdout.write(f' {text}')

# python manage.py get_all_orders_by_product_id 18