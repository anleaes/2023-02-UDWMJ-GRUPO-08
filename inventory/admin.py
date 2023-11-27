from django.contrib import admin
from .models import Item, Player, Inventory, Adventure

admin.site.register(Item)
admin.site.register(Player)
admin.site.register(Inventory)
admin.site.register(Adventure)