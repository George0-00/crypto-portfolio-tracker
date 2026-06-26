from django.db import models
from django.conf import settings


class Asset(models.Model):
    SYMBOLS = [
        ('BTC', 'Bitcoin'),
        ('ETH', 'Ethereum'),
        ('SOL', 'Solana'),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    symbol = models.CharField(max_length=10, choices=SYMBOLS)
    amount = models.DecimalField(max_digits=18, decimal_places=8)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.symbol}"


class Transaction(models.Model):
    BUY = 'buy'
    SELL = 'sell'

    TYPE_CHOICES = [
        (BUY, 'Buy'),
        (SELL, 'Sell'),
    ]
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    symbol = models.CharField(max_length=10)  # BTC, ETH и т.д.
    type = models.CharField(max_length=4, choices=TYPE_CHOICES)
    amount = models.DecimalField(max_digits=18, decimal_places=8)
    price = models.DecimalField(max_digits=18, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return f"{self.user.username} {self.type} {self.symbol}"