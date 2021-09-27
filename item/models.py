from django.db import models

from account.models import User


class Category(models.Model):
    name = models.CharField('Наименование', max_length=256)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Item(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='items',
        verbose_name='Владелец',
        blank=True,
        null=True,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='items',
        verbose_name='Категория',
        blank=True,
        null=True
    )
    name = models.CharField('Название', max_length=256, blank=True, null=True)
    brand = models.CharField('Бренд', max_length=256, blank=True, null=True)
    size = models.CharField('Размер', max_length=256, blank=True, null=True)
    barcode = models.CharField('Баркод', max_length=256, blank=True, null=True)
    stock = models.IntegerField('Остаток', default=0)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
