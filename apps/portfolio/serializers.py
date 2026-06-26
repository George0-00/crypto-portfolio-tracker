from rest_framework import serializers
from .models import Transaction


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'symbol', 'type', 'amount', 'price', 'created_at']
        read_only_fields = ['id', 'created_at']
