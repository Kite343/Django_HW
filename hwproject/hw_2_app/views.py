from django.shortcuts import get_object_or_404, render

from django.http import HttpResponse, HttpResponseNotFound
import logging
from datetime import date, datetime, timedelta

from .models import *

logger = logging.getLogger(__name__)

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
]

def clients(request):
    clients = Client.objects.all()

    context = {
        'clients': clients,
        'menu': menu,
        'title': 'Главная страница',
    }
 
    return render(request, 'hw_2_app/clients.html', context=context)


def show_client(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    context = {
        'client': client,
        'menu': menu,
        'title': 'Клиент',
    }
    return render(request, 'hw_2_app/client_id.html', context=context)

def client_orders(request, client_id):
    # client = get_object_or_404(Client, pk=client_id)
    now = datetime.now()
    week = now - timedelta(days=7)
    month = now - timedelta(days=30)
    year = now - timedelta(days=365)

    orders_week = Order.objects.\
                filter(client__pk=client_id, time_create__gte=week, time_create__lte=now).\
                order_by('time_create')
    
    orders_month = Order.objects.\
                filter(client__pk=client_id, time_create__gte=month, time_create__lte=week).\
                order_by('time_create')
    
    orders_year = Order.objects.\
                filter(client__pk=client_id, time_create__gte=year, time_create__lte=month).\
                order_by('time_create')
    
    context = {'menu': menu,
            'title': 'Заказы клиента',
            "orders_week": orders_week, 
            "orders_month": orders_month,
            "orders_year": orders_year}

    return render(request, 'hw_2_app/client_orders.html', context=context)

def client_products(request, client_id):
    # client = get_object_or_404(Client, pk=client_id)
    now = datetime.now()
    week = now - timedelta(days=7)
    month = now - timedelta(days=30)
    year = now - timedelta(days=365)
    # orders_week = Order.objects.filter(client__pk=client_id, time_create__gte=week, time_create__lte=now).order_by(
    #     'time_create')
    orders_week = Order.objects.\
                filter(client__pk=client_id,time_create__gte=week).\
                order_by('time_create')
    
    orders_month = Order.objects.\
                filter(client__pk=client_id,
                       time_create__gte=month,
                       time_create__lte=week).\
                order_by('time_create')
    
    orders_year = Order.objects.\
                filter(client__pk=client_id,
                        time_create__gte=year,
                        time_create__lte=month).\
                order_by('time_create')    
    
    products_week = {p for orders in orders_week for p in orders.product.all()}
    products_month = {p for orders in orders_month for p in orders.product.all()}.\
                    difference(products_week)
    products_year = {p for orders in orders_year for p in orders.product.all()}.\
                    difference(products_week).difference(products_month)

    context = {'menu': menu,
            'title': 'Продукты заказанные клиентом',
            "products_week": products_week, 
            "products_month": products_month,
            "products_year": products_year}
    
    return render(request, 'hw_2_app/client_products.html', context=context)

def index(request):
    products = Product.objects.all()

    context = {
        'products': products,
        'menu': menu,
        'title': 'Главная страница',
    }
 
    return render(request, 'hw_2_app/index.html', context=context)

def show_product(request, product_id):
    return HttpResponse(f"Отображение продукта с id = {product_id}")

def about(request):
    return render(request, 'hw_2_app/about.html', {'menu': menu, 'title': 'О сайте'})
 
def contact(request):
    return HttpResponse("Обратная связь")
 
def login(request):
    return HttpResponse("Авторизация")

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
