from django.db import models
from django.urls import reverse

class Client(models.Model):
    name = models.CharField(max_length=100, verbose_name="имя")
    email = models.EmailField(verbose_name="электронная почта")
    phone = models.TextField(verbose_name="телефон")
    address = models.TextField(verbose_name="адресс")
    registration_date = models.DateTimeField(auto_now_add=True, verbose_name="дата регистрации")

    def __str__(self):
        return f'{self.name}: email {self.email}, phone number {self.phone}'
    
    def get_absolute_url(self):
        return reverse('client', kwargs={'client_id': self.pk})
    
    class Meta:
        verbose_name = 'Клиентов'
        verbose_name_plural = 'Клиенты'
        ordering = ['name', 'registration_date']

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото", blank=True)
    description = models.TextField(verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    quantity = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Количество")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="дата добавления")

    def __str__(self):
        return f"Product {self.name}, price {self.price}"
    
    def get_absolute_url(self):
        return reverse('product', kwargs={'product_id': self.pk})
    
    class Meta:
        verbose_name = 'Продукты'
        verbose_name_plural = 'Продукты'
        # ordering = ['name', 'time_create']


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name="клиент")
    product = models.ManyToManyField(Product, verbose_name="продукты")
    total_amount = models.DecimalField(default=0, max_digits=10, decimal_places=2, verbose_name="сумма")
    time_create = models.DateTimeField(auto_now=True, verbose_name="дата создания")

    def __str__(self):
        return f'Order: client {self.client}, time_create {self.time_create}'
    
    class Meta:
        verbose_name = 'Сделки'
        verbose_name_plural = 'Сделки'
        # ordering = ['client', 'time_create']
    
    # python manage.py makemigrations hw_2_app
    # python manage.py migrate