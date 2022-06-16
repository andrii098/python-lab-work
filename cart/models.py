from django.db import models
from django.core.validators import RegexValidator
from shop.models import Item

class Order(models.Model):
    client_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    goods_ids = models.ManyToManyField(Item, related_name='goods_ids')

    def ids_str(self):
    	list_goods = list(self.goods_ids.all())
    	ids = []
    	for good in list_goods:
    		ids.append(good.id)

    	return str(ids)

    def full_price(self):
    	list_goods = list(self.goods_ids.all())
    	sum = 0
    	for good in list_goods:
    		sum += good.price

    	return sum


# Create your models here.
