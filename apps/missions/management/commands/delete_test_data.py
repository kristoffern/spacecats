from django.core.management.base import BaseCommand
from missions.models import Mission
from spacecats.models import SpaceCat

class Command(BaseCommand):
    help = "Delete all test data for SpaceCats and Mission models"

    def handle(self, *args, **options):
        
        SpaceCat.objects.all().delete()
        Mission.objects.all().delete()
        