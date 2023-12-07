from django.shortcuts import render, get_object_or_404, redirect
from .forms import InventoryForm, InventoryItemForm
from .models import Inventory , InventoryItem, Item, Player
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/contas/login/')
def add_inventory(request, id_player):
    template_name = 'inventories/add_inventory.html'
    context = {}
    if request.method == 'POST':
        form = InventoryForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.player = Player.objects.get(id=id_player)
            f.save()
            form.save_m2m()
            return redirect('inventories:list_inventories')
    form = InventoryForm()
    context['form'] = form
    return render(request, template_name, context)

def list_inventories(request):
    template_name = 'inventories/list_inventories.html'
    inventories = Inventory.objects.filter()
    inventory_items = InventoryItem.objects.filter()
    items = Item.objects.filter()
    players = Player.objects.filter()
    context = {
        'inventories': inventories,
        'inventory_items': inventory_items,
        'items': items,
        'players': players
    }
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def delete_inventory(request, id_inventory):
    inventory = Inventory.objects.get(id=id_inventory)
    inventory.delete()
    return redirect('inventories:list_inventories')

@login_required(login_url='/contas/login/')
def add_inventory_item(request, id_inventory):
    template_name = 'inventories/add_inventory_item.html'
    context = {}
    if request.method == 'POST':
        form = InventoryItemForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.inventory = Inventory.objects.get(id=id_inventory)
            f.save()
            form.save_m2m()
            return redirect('inventories:list_inventories')
    form = InventoryItemForm()
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def delete_inventory_item(request, id_inventory_item):
    inventoryitem = InventoryItem.objects.get(id=id_inventory_item)
    inventoryitem.delete()
    return redirect('inventories:list_inventories')

@login_required(login_url='/contas/login/')
def edit_inventory_status(request, id_inventory):
    template_name = 'inventories/edit_inventory_status.html'
    context ={}
    inventory = get_object_or_404(Inventory, id=id_inventory)
    if request.method == 'POST':
        form = InventoryForm(request.POST, instance=inventory)
        if form.is_valid():
            form.save()
            return redirect('inventories:list_inventories')
    form = InventoryForm(instance=inventory)
    context['form'] = form
    return render(request, template_name, context)