from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Валюта
class Currency(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, verbose_name='slug', unique=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']  # сортировка
        verbose_name = 'Валюта'
        verbose_name_plural = 'Валюты'


# Тип ценной бумаги
class SecurityType(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, verbose_name='slug', unique=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']  # сортировка
        verbose_name = 'Тип ценной бумаги'
        verbose_name_plural = 'Типы ценных бумаг'


# Ценная бумага
class Securities(models.Model):

    type_securities = models.ForeignKey(SecurityType, on_delete=models.PROTECT,
                              related_name='securitytype', verbose_name='Тип ценной бумаги')
    image = models.ImageField(verbose_name='Изображение', upload_to='photos/%Y/%m/%d/', blank=True)
    ticker = models.SlugField(unique=True, verbose_name='Тикер') # выполняет функцию slug
    name = models.CharField(max_length=150, verbose_name='Название')
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT, related_name='currency', verbose_name='Валюта')

    def __str__(self):
        return f'{self.type_securities}:{self.name} [{self.currency}]'
    # def __str__(self):
    #     return self.ticker

    class Meta:
        ordering = ['ticker']  # сортировка
        verbose_name = 'Ценная бумага'
        verbose_name_plural = 'Ценные бумаги'


# Инвестор
class InvestorUser(models.Model):

    title = models.CharField(max_length=255, verbose_name='Тип счета')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=255, verbose_name='slug', unique=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        ordering = ['last_name']  # сортировка
        verbose_name = 'Инвестор'
        verbose_name_plural = 'Инвесторы'


# Открытая позиция
class Position(models.Model):

    slug = models.SlugField(max_length=255, verbose_name='открытая позиция', unique=True)
    security = models.ForeignKey(Securities, on_delete=models.PROTECT,
                                 related_name='security', verbose_name='Ценная бумага')
    quantity = models.DecimalField(max_digits=9, decimal_places=0, verbose_name='Количество')
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена за штуку')
    investor = models.ForeignKey(InvestorUser, on_delete=models.PROTECT,
                                 related_name='investor', verbose_name='Инвестор')

    def __str__(self):
        return self.slug

    class Meta:
        ordering = ['investor']  # сортировка
        verbose_name = 'Открытая позиция'
        verbose_name_plural = 'Открытые позиции'
