from django.contrib import admin
from .models import Stock

class StockAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'buy_price', 'sell_price', 'total_shares', 'is_active', 'updated_at', 'created_at')

admin.site.register(Stock, StockAdmin)
