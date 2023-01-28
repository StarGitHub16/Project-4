from django.contrib import admin

# Register your models here.

class StocksAdmin(admin.ModelAdmin):
    list_display = ('Stock', 'Quantity', 'Value','Buy/Sell')