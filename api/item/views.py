from rest_framework import viewsets

from api.item.serializers import ItemSerializer
from item.models import Item


class ItemViewSet(viewsets.ModelViewSet):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()
