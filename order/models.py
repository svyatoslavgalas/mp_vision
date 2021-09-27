from django.db import models

from account.models import User
from item.models import Item


class Order(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='orders',
        verbose_name='Пользователь'
    )
    item = models.ForeignKey(
        Item,
        on_delete=models.CASCADE,
        related_name='orders',
        verbose_name='Товар',
        blank=True,
        null=True
    )
    wb_order_id = models.CharField('Вб order_id', max_length=256, blank=True, null=True)
    date_created = models.CharField('Дата создания заказа', max_length=256, blank=True, null=True)
    pid = models.CharField('Вб pid', max_length=256, blank=True, null=True)
    profit = models.PositiveIntegerField('Прибыль', default=0, blank=True, null=True)
    proceeds = models.PositiveIntegerField('Выручка', default=0, blank=True, null=True)

