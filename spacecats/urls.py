from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from django.urls import re_path
from apps.missions.views import create_test_data_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('create-test-data/', create_test_data_view, name='create_test_data'),
    re_path('^', include('apps.spacecats.urls')),
]
