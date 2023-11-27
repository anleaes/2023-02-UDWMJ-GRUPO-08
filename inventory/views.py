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

    # Lógica para calcular os pontos ganhos e itens perdidos na aventura
    points_earned = calcular_pontos_aventura()
    items_lost = calcular_itens_perdidos()

    # Atualizar pontos do jogador
    player.points += points_earned
    player.save()

    # Associar itens perdidos ao jogador
    for item in items_lost:
        Adventure.objects.create(player=player, points_earned=points_earned, items_lost=item)

    context = {'player': player, 'points_earned': points_earned, 'items_lost': items_lost}
    return render(request, 'inventory/adventure.html', context)

def buy_item(request, item_id):
    player = Player.objects.get(pk=1)  # Assumindo que há um jogador com ID 1
    item = Item.objects.get(pk=item_id)
    
    if player.points >= item.points:
        player.points -= item.points
        player.save()
        Inventory.objects.create(player=player, item=item)

    return redirect('market')

def index(request):
    return render(request, 'inventory/index.html')

def calcular_pontos_aventura():
    # Implemente a lógica para calcular os pontos ganhos na aventura
    # Exemplo: retorne um valor fixo ou calcule com base em algum critério específico
    return 10  # Ajuste conforme necessário

def calcular_itens_perdidos():
    # Implemente a lógica para calcular os itens perdidos na aventura
    # Exemplo: retorne uma lista de itens ou calcule com base em algum critério específico
    items_perdidos = Item.objects.filter(name__icontains='Espada')  # Ajuste conforme necessário
    return items_perdidos
