from bar.models import Order, Table
from rest_framework import serializers


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ('url', 'name', 'email', 'table', 'date')  

class TableSerializer(serializers.ModelSerializer):
    orders = OrderSerializer(many=True, read_only=True)

    class Meta:
        model = Table
        fields = ('id', 'seats', 'orders')