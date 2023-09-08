from django import forms
from django.contrib import admin

from hw_2_app.models import *

import logging

logger = logging.getLogger(__name__)

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'address', 'registration_date']
    readonly_fields = ['registration_date', ]
    search_fields = ['name']
    search_help_text = 'Поиск по имени'
    list_display_links = ['name']

@admin.action(description="Сбросить количество в ноль")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'photo', 'description', 'price', 'quantity']
    readonly_fields = ['id', 'time_create', ]
    ordering = ['name', 'price', 'quantity', ]
    search_fields = ['name', 'description', ]
    search_help_text = 'Поиск по имени и описанию'
    list_display_links = ['name', 'description']
    actions = [reset_quantity]


class ProductshipInline(admin.TabularInline):
    model = Order.product.through

 
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [
        ProductshipInline,
    ]
    list_display = ['id', 'client', 'total_amount', 'time_create']
    readonly_fields = ['id', 'time_create', ]
    ordering = ['client', 'time_create', ]
    search_fields = ['client', ]
    search_help_text = 'Поиск по имени'
    list_display_links = ['id', 'client']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['id', 'client', ],
            },
        ),
        # (
        #     'Продукты',
        #     {
        #         'classes': ['collapse'],
        #         'description': 'Продукты',
        #         'fields': ['product'],
        #     },
        # ),
        (
            'Инфорация',
            {
                'description': 'Информация',
                'fields': ['total_amount', 'time_create', ],
            }
        ),
        
    ]

