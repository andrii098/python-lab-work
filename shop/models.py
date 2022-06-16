from django.db import models

class Item(models.Model):
	name = models.CharField(max_length=100)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	description = models.CharField(max_length=1000)
	photo = models.ImageField(upload_to='goods_photos', 
							default='goods_photos/no-photo.png')

# Create your models here.
