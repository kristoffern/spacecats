from django.shortcuts import render
from django.views.generic import ListView
from .models import SpaceCat

class CrewListView(ListView):
    model = SpaceCat
    template_name = 'spacecats/crew_list.html'
    context_object_name = 'spacecats'
