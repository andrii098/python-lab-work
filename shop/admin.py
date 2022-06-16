from django.contrib import admin

from shop.models import Item

class ItemAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'price')


admin.site.register(Item, ItemAdmin)

# Register your models here.
