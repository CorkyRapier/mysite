from django.db import models
from django.db.models.fields import SlugField

class Category(models.Model):

    name = models.CharField(max_length=255, verbose_name='Имя категории')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя продукта')



#проверяю гит

# 1. Товар
# 2. Категория товара
# 3.КартПродукт
# 4.Корзина
# 5.Заказ
# 6.Кастомюзер
# 7.Спецификации
