import random
from datetime import date, timedelta
from django.core.management.base import BaseCommand
from missions.models import SpaceCat, Mission

class Command(BaseCommand):
    help = 'Create test data for SpaceCat and Mission models'

    def handle(self, *args, **kwargs):
        roles = ['Tester', 'Developer', 'Project Lead', 'Manager']
        names = ['Fluffy', 'Whiskers', 'Shadow', 'Smokey', 'Luna']

        # Create SpaceCats
        for _ in range(10):
            name = random.choice(names)
            role = random.choice(roles)
            age = random.randint(1, 15)
            mission_count = random.randint(0, 5)
            SpaceCat.objects.create(name=name, role=role, age=age, mission_count=mission_count)

        # Create Missions
        for _ in range(5):
            mission_name = f"Mission {random.randint(1, 100)}"
            description = "A mission to explore the unknown regions of space."
            launch_date = date.today() - timedelta(days=random.randint(0, 365))
            mission = Mission.objects.create(name=mission_name, description=description, launch_date=launch_date)
            mission.spacecats.set(SpaceCat.objects.order_by('?')[:3])

        self.stdout.write(self.style.SUCCESS('Successfully created test data'))
