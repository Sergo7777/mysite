from django.shortcuts import render
from bar.models import Order, Table
from rest_framework import viewsets
from rest.serializers import OrderSerializer, TableSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('date')
    serializer_class = OrderSerializer

class TableViewSet(viewsets.ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer