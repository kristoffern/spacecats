from django.contrib import admin
from django.urls import path
from .views import CrewListView, SpaceCatDetailView
from missions.views import (
    MissionDetailView,
    MissionListView,
    create_test_data_view,
    delete_test_data_view,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('crew/', CrewListView.as_view(), name='crew-list'),
    path('crew/<int:pk>/', SpaceCatDetailView.as_view(), name='spacecat-detail'),
    path('missions/', MissionListView.as_view(), name='mission-list'),
    path('missions/<int:pk>/', MissionDetailView.as_view(), name='mission-detail'),
    path('create-test-data/', create_test_data_view, name='create_test_data'),
    path('delete-test-data/', delete_test_data_view, name='delete_test_data'),
]
