from .models import Transaction
from django.db.models import Sum


def get_user_portfolio(user):
    transactions = Transaction.objects.filter(user=user)

    portfolio = {}

    for tx in transactions:
        symbol = tx.symbol

        if symbol not in portfolio:
            portfolio[symbol] = {
                "amount": 0,
                "invested": 0
            }

        if tx.type == "buy":
            portfolio[symbol]["amount"] += float(tx.amount)
            portfolio[symbol]["invested"] += float(tx.amount) * float(tx.price)

        elif tx.type == "sell":
            portfolio[symbol]["amount"] -= float(tx.amount)
            portfolio[symbol]["invested"] -= float(tx.amount) * float(tx.price)

    return portfolio