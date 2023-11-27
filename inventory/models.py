# inventory/models.py

from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    points = models.IntegerField()

class Player(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, default='Male')  # Defina o valor padrão como 'Male'
    points = models.IntegerField(default=100)

class Inventory(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

class Adventure(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    points_earned = models.IntegerField()
    items_lost = models.ManyToManyField(Item)
