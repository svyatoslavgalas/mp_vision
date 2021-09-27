from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .account.views import (SignupViewSet)
from .item.views import ItemViewSet
from .order.views import OrderViewSet
from .parser.views import (
    ParseOrdersViewSet,
    ParseItemViewSet,
)

router = DefaultRouter()
router.register('signup', SignupViewSet, basename='signup')
router.register('parse-order', ParseOrdersViewSet, basename='parse-order')
router.register('parse-item', ParseItemViewSet, basename='parse-item')
router.register('stock', ItemViewSet, basename='stock')
router.register('order', OrderViewSet, basename='order')

urlpatterns = [
    path('', include(router.urls)),
]
