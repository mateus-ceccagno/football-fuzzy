from django.shortcuts import render, redirect

from nflscoreapp.forms import JogadorForm
from nflscoreapp.fuzzy import classificacao
from nflscoreapp.models import Jogador
# from fuzzy import classificacao

# Create your views here.
def home(request):
    return render(request, 'index.html')

def form(request):
    data = {}
    data['form'] = JogadorForm()
    return render(request, 'form.html', data)

def create(request):
    form = JogadorForm(request.POST or None)
   
    # For some reason, you're re-instantiating the form after you check is_valid().
    # Forms only get a cleaned_data attribute when is_valid() has been called, 
    # and you haven't called it on this new, second instance.
    if form.is_valid():
        vitorias = form.cleaned_data['vitorias']

    vitorias = form.cleaned_data['vitorias']
    touchdowns = form.cleaned_data['touchdowns']
    jardas = form.cleaned_data['jardas']
    recepcoes = form.cleaned_data['recepcoes']
    form.cleaned_data['resultado'] = classificacao(vitorias, touchdowns, jardas, recepcoes)    

    if form.is_valid():
        form.save()
        
    # obtém o resultado fuzzy
    
    return redirect('ranking')

def ranking(request):
    data = {}
    data['dbs'] = Jogador.objects.all()
    return render(request, 'list.html', data)

def view(request, pk):
    data = {}
    data['db'] = Jogador.objects.get(pk=pk)
    return render(request, 'view.html', data)

def edit(request, pk):
    data = {}
    data['db'] = Jogador.objects.get(pk=pk)
    data['form'] = JogadorForm(instance=data['db'])
    return render(request, 'form.html', data)

def update(request, pk):
    data = {}
    data['db'] = Jogador.objects.get(pk=pk)
    form = JogadorForm(request.POST or None, instance=data['db'])

    # For some reason, you're re-instantiating the form after you check is_valid().
    # Forms only get a cleaned_data attribute when is_valid() has been called, 
    # and you haven't called it on this new, second instance.
    if form.is_valid():
        vitorias = form.cleaned_data['vitorias']
        
    vitorias = form.cleaned_data['vitorias']
    touchdowns = form.cleaned_data['touchdowns']
    jardas = form.cleaned_data['jardas']
    recepcoes = form.cleaned_data['recepcoes']

    if form.is_valid():
        obj = form.save(commit=False)
        obj.resultado = classificacao(vitorias, touchdowns, jardas, recepcoes)  
        obj.save()
        return redirect('ranking')

def delete(request, pk):
    db = Jogador.objects.get(pk=pk)
    db.delete()
    return redirect('ranking')