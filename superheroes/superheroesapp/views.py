from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Superhero
from .forms import superhero_forms

# Create your views here.

def index(request):

    all_superheroes = Superhero.objects.all()
    context = {
        'all_superheroes': all_superheroes
    }

    return render(request, 'superheroesapp/index.html', context)