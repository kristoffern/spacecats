import random
import datetime

from django.core.management.base import BaseCommand
from missions.models import Mission
from spacecats.models import SpaceCat

class Command(BaseCommand):
    help = "Create test data for SpaceCats and Mission models"

    def handle(self, *args, **options):
        roles = ['Tester', 'Developer', 'Manager', 'Project Lead']
        names = ['Fluffy', 'Whiskers', 'Shadow', 'Luna', 'Smokey']

        for _ in range(10):
            name = random.choice(names)
            role = random.choice(roles)
            age = random.randint(1,20)
            mission_count = random.randint(0,5)

            SpaceCat.objects.create(name=name, age=age, role=role, mission_count=mission_count)

        for _ in range(5):
            mission_name = f"Mission {random.randint(1,100)}"
            description = f"A mission to explore the unknown regions of space."
            launch_date = datetime.date.today() - datetime.timedelta(days=random.randint(0,365))

            mission = Mission.objects.create(name=mission_name, description=description, launch_date=launch_date)
            mission.spacecats.set(SpaceCat.objects.order_by('?')[:3])