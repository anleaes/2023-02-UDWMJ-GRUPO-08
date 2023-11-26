# inventory/views.py
from django.shortcuts import render, redirect
from .models import Item, Player, Inventory, Adventure

def market(request):
    player = Player.objects.get(pk=1)  # Assumindo que há um jogador com ID 1
    items = Item.objects.all()
    context = {'player': player, 'items': items}
    return render(request, 'inventory/market.html', context)

def adventure(request):
    player = Player.objects.get(pk=1)  # Assumindo que há um jogador com ID 1
    context = {'player': player}
    return render(request, 'inventory/adventure.html', context)

def buy_item(request, item_id):
    player = Player.objects.get(pk=1)  # Assumindo que há um jogador com ID 1
    item = Item.objects.get(pk=item_id)
    
    if player.points >= item.points:
        player.points -= item.points
        player.save()
        Inventory.objects.create(player=player, item=item)

    return redirect('market')