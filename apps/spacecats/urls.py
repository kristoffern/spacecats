from django.urls import path
from apps.spacecats.views import CrewListView

urlpatterns = [
    path('crew/', CrewListView.as_view(), name='crew-list'),
]