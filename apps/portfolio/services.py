from .models import Transaction
from django.db.models import Sum


CURRENT_PRICES = {
    "BTC": 45000,
    "ETH": 2500,
    "SOL": 100
}


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

    #  добавляем PnL
    for symbol, data in portfolio.items():
        current_price = CURRENT_PRICES.get(symbol, 0)

        current_value = data["amount"] * current_price
        invested = data["invested"]

        pnl = current_value - invested
        roi = (pnl / invested * 100) if invested else 0

        data["current_price"] = current_price
        data["current_value"] = current_value
        data["pnl"] = pnl
        data["roi_percent"] = roi

    return portfolio
