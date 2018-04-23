from django.contrib import admin
from transaction.models import Transaction, Request
# Register your models here.
admin.site.register(Transaction)
admin.site.register(Request)
