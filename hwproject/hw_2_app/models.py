from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.TextField()
    address = models.TextField()
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}: email {self.email}, phone number {self.phone}'

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    time_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Product {self.name}, price {self.price}"


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)
    total_amount = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    time_create = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Order: client {self.client}, product {self.product}'
    
    # python manage.py makemigrations hw_2_app
    # python manage.py migrate



