from django.contrib import admin
from django.urls import path
from .views import CrewListView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('crew/', CrewListView.as_view(), name='crew-list'),
]
