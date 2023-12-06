from django.db import models
from items.models import Item
from players.models import Player

# Create your models here.

class Inventory(models.Model):
    STATUS_CHOICES = (
        ('Ativo', 'Ativo'),
        ('Inativo', 'Inativo'),
    )
    status = models.CharField('Status', max_length=20, choices=STATUS_CHOICES, null=True, blank=True, default='Ativo')
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    inventory_item = models.ManyToManyField(Item, through='InventoryItem', blank=True)
    
    class Meta:
        verbose_name = 'Inventario'
        verbose_name_plural = 'Inventarios'
        ordering =['id']

    def __str__(self):
        return "%s" % (self.status) 


class InventoryItem(models.Model):
    quantity = models.IntegerField('Quantidade',null=True, blank=True,default=0)
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Item do inventario'
        verbose_name_plural = 'Itens do inventario'
        ordering =['id']

    def __str__(self):
        return "%s" % (self.quantity) 