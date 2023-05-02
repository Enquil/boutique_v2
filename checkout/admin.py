from django.contrib import admin
from .models import Order, OrderLineItem


class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('order_numer',
                       'date',
                       'delivery_cost',
                       'order_total',
                       'grand_total',)

    fields = ('order_number',
              'date',
              'full_name',
              'email',
              'phone_number',
              'country',
              'post_code',
              'town_or_city',
              'street_adress1',
              'street_adress2',
              'county',
              'delivery_cost',
              'order_total',
              'grand_total',)

    list_display = ('order_number',
                    'date',
                    'full_name',
                    'order_total',
                    'delivery_cost',
                    'grand_total',)
    
    ordering = ('-date',)
