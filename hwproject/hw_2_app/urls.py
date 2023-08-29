from django.urls import path, re_path

from .views import *

urlpatterns = [
    # path('', index, name='index'),
    path('', index, name='home'),
    path('about/', about, name='about'),
    # path('addpage/', addpage, name='add_page'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('product/<int:product_id>/', show_product, name='product'),
    path('clients', clients, name='clients'),
    path('client/<int:client_id>/', show_client, name='client'),
    path('client_orders/<int:client_id>/', client_orders, name='client_orders'),
    path('client_products/<int:client_id>/', client_products, name='client_products'),
]