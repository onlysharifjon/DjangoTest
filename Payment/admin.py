from django.contrib import admin

# Register your models here.
from .models import Card,PayHistory
admin.site.register(Card,list_display = ['card_holder','card_number','expired_date','money'])
admin.site.register(PayHistory,list_display = ['name','total_money','where','time'])