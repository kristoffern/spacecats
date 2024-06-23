import logging
from django.shortcuts import render
from django.views.generic import ListView
from .models import SpaceCat

logger = logging.getLogger(__name__)

class CrewListView(ListView):
    model = SpaceCat
    template_name = 'spacecats/crew_list.html'
    context_object_name = 'spacecats'

    def get(self, request, *args, **kwargs):
        logger.info("Crew list view called")
        logger.info(f"{SpaceCat.objects.count()} SpaceCats in the crew")
        return super().get(request, *args, **kwargs)
