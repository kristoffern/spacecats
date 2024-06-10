from django.contrib import admin
from django.urls import path
from .views import CrewListView
from missions.views import create_test_data_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('crew/', CrewListView.as_view(), name='crew-list'),
    path('create-test-data/', create_test_data_view, name='create_test_data'),
]
