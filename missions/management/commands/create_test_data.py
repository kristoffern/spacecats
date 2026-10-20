from django.core.management.base import BaseCommand

from missions.sample_data import create_sample_data


class Command(BaseCommand):
    help = "Create test data for SpaceCats and Mission models"

    def handle(self, *args, **options):
        cats, missions = create_sample_data()

        for cat in cats:
            self.stdout.write(f"  cat: {cat.name} ({cat.role}), age {cat.age}, missions {cat.mission_count}")
        for m in missions:
            crew = ", ".join(c.name for c in m.spacecats.all())
            self.stdout.write(f"  mission: {m.name} launched {m.launch_date} crew [{crew}]")
        self.stdout.write(self.style.SUCCESS(f"Created {len(cats)} SpaceCats and {len(missions)} Missions"))
