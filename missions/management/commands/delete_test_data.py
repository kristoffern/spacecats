from django.core.management.base import BaseCommand

from missions.sample_data import delete_sample_data


class Command(BaseCommand):
    help = "Delete all test data for SpaceCats and Mission models"

    def handle(self, *args, **options):
        cats, missions = delete_sample_data()
        self.stdout.write(self.style.SUCCESS(f"Deleted {cats} SpaceCats and {missions} Missions"))
