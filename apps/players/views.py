from django.shortcuts import render, get_object_or_404, redirect
from .forms import PlayerForm
from .models import Player
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/contas/login/')
def add_player(request):
    template_name = 'players/add_player.html'
    context = {}
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('players:list_players')
    form = PlayerForm()
    context['form'] = form
    return render(request, template_name, context)
    
@login_required(login_url='/contas/login/')
def list_players(request):
    template_name = 'players/list_players.html'
    players = Player.objects.filter()
    context = {
        'players': players
    }
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def edit_player(request, id_player):
    template_name = 'players/add_player.html'
    context ={}
    player = get_object_or_404(Player, id=id_player)
    if request.method == 'POST':
        form = PlayerForm(request.POST, instance=player)
        if form.is_valid():
            form.save()
            return redirect('players:list_players')
    form = PlayerForm(instance=player)
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def delete_player(request, id_player):
    player = Player.objects.get(id=id_player)
    player.delete()
    return redirect('players:list_players')

def search_players(request):
    template_name = 'players/list_players.html'
    query = request.GET.get('query')
    players = Player.objects.filter(name__icontains=query)
    context = {
        'players': players,
    }
    return render(request,template_name, context)