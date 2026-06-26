from django.urls import path
from .views import TransactionListCreateView, portfolio_view

urlpatterns = [
    path('transactions/', TransactionListCreateView.as_view()),
    path('portfolio/', portfolio_view),
]
