from rest_framework import viewsets
from rest_framework.response import Response

from api.order.serializers import OrderSerializer
from item.models import Item
from order.models import Order


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def list(self, request, *args, **kwargs):
        user = request.user
        data = {}
        orders = Order.objects.filter(owner=user)
        for order in orders:
            if order.item.category.name not in data.keys():
                data[order.item.category.name] = {}
            if order.item.name not in data[order.item.category.name].keys():
                data[order.item.category.name][order.item.name] = {
                    'Заказов': 0,
                    'Прибыль': 0,
                }
            data[order.item.category.name][order.item.name]['Заказов'] += 1
            data[order.item.category.name][order.item.name]['Прибыль'] += order.profit
        return Response(data)
