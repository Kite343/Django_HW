from django.db import models
from django.urls import reverse

class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.TextField()
    address = models.TextField()
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}: email {self.email}, phone number {self.phone}'
    
    def get_absolute_url(self):
        return reverse('client', kwargs={'client_id': self.pk})

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото", blank=True)
    description = models.TextField(verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    quantity = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Количество")
    time_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Product {self.name}, price {self.price}"
    
    def get_absolute_url(self):
        return reverse('product', kwargs={'product_id': self.pk})


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)
    total_amount = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    time_create = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Order: client {self.client}, product {self.product}'
    
    # python manage.py makemigrations hw_2_app
    # python manage.py migrate



