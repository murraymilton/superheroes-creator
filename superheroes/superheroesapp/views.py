from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Superhero
from .forms import superhero_forms

# Create your views here.


def create_new_superhero(request):
    if request.method == 'POST':
        superhero_name = request.POST.get('name')
        superhero_alter_ego = request.POST.get('alter_ego')
        superhero_primary_ability = request.POST.get('primary_superhero_ability')
        superhero_secondary_ability = request.POST.get('secondary_superhero_ability')
        superhero_catchphrase = request.POST.get('superhero_catchphrase')
        new_superhero = Superhero(superhero_name=superhero_name, alter_ego_name=superhero_alter_ego, primary_hero_ability=superhero_primary_ability, secondary_hero_ability=superhero_secondary_ability, superhero_catchphrase=superhero_catchphrase)
        new_superhero.save()

        return HttpResponseRedirect(reverse('superheroesapp:index'))
    else:
        return render(request, 'superheroesapp/index.html')


def index(request):

    all_superheroes = Superhero.objects.all()
    context = {
        'all_superheroes': all_superheroes
    }

    return render(request, 'superheroesapp/index.html', context)


def display_data(request, superhero_id):
    superhero_data = Superhero.objects.get(pk=superhero_id)
    context = {
        'superhero_data': superhero_data
    }
    return render(request, "superheroesapp/display.html", context)


def superhero_edit(request, superhero_id):
    superhero_edit_information = Superhero.objects.get(pk=superhero_id)
    context = {
        'superhero_update': superhero_edit_information
    }
    return render(request, "superheroesapp/edit.html", context)


def update_superhero(request, superhero_id):
    superhero_update = Superhero.objects.get(pk=superhero_id)
    form = superhero_forms(request.POST, instance=superhero_update)
    if form.is_valid():
        form.save()
        return redirect('/')
    context = {
        'form': form
    }
    return render(request, "superheroesapp/edit.html", context)


def delete_superhero(request, superhero_id):
    superhero_delete = Superhero.objects.get(pk=superhero_id)
    superhero_delete.delete()
    context = {
        'superhero_delete': superhero_delete
    }
    return redirect('/')