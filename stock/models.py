from django.db import models

class Stock(models.Model):
    name = models.CharField(max_length=255)
    code = models.IntegerField(unique=True)
    buy_price = models.FloatField(default=0)
    sell_price = models.FloatField(default=0)
    total_shares = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
