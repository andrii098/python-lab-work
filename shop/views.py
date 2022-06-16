from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from shop.models import Item

def index(request):
	goods = Item.objects.all()
	
	template = loader.get_template('shop/index.html')
	context = {
		'goods': goods, 
	}
	return HttpResponse(template.render(context))    


# Create your views here.

