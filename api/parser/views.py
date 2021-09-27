from rest_framework import viewsets
from rest_framework.response import Response

from item.models import Item, Category
from order.models import Order
from tools.parser import Parser


class ParseItemViewSet(viewsets.ModelViewSet):

    def list(self, request, *args, **kwargs):
        data = {'result': True}
        user = request.user
        parser = Parser(user.wb_token)
        wb_items = parser.parse_items()
        if wb_items['stocks']:
            for wb_item in wb_items['stocks']:
                item, _ = Item.objects.get_or_create(
                    owner=user,
                    barcode=wb_item['barcode']
                )
                category, _ = Category.objects.get_or_create(
                    name=wb_item['subject']
                )
                item.category = category
                item.name = wb_item['name']
                item.brand = wb_item['brand']
                item.size = wb_item['size']
                item.stock = wb_item['stock']
                item.save()
        return Response(data)


class ParseOrdersViewSet(viewsets.ModelViewSet):

    def list(self, request, *args, **kwargs):
        data = {'result': True}
        user = request.user
        parser = Parser(user.wb_token)
        wb_orders = parser.parse_orders()
        if wb_orders['orders']:
            for wb_order in wb_orders['orders']:
                order, _ = Order.objects.get_or_create(
                    owner=user,
                    wb_order_id=wb_order['orderId']
                )
                item = Item.objects.get(barcode=wb_order['barcode'])
                order.item = item
                order.date_created = wb_order['dateCreated']
                order.pid = wb_order['pid']
                order.profit = wb_order['totalPrice']
                order.save()
        return Response(data)
