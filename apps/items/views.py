from django.shortcuts import render, get_object_or_404, redirect
from .forms import ItemForm
from .models import Item
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/contas/login/')
def add_item(request):
    template_name = 'items/add_item.html'
    context = {}
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('items:list_items')
    form = ItemForm()
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def list_items(request):
    template_name = 'items/list_items.html'
    item = Item.objects.filter()
    context = {
        'items': item
    }
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def edit_item(request, id_item):
    template_name = 'items/add_item.html'
    context ={}
    item = get_object_or_404(Item, id=id_item)
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES,  instance=item)
        if form.is_valid():
            form.save()
            return redirect('items:list_items')
    form = ItemForm(instance=item)
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def delete_item(request, id_item):
    item = item.objects.get(id=id_item)
    item.delete()
    return redirect('items:list_items')