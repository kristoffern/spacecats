import datetime
import random

from missions.models import Mission
from spacecats.models import SpaceCat

ROLES = ['Tester', 'Developer', 'Manager', 'Project Lead']
NAMES = ['Fluffy', 'Whiskers', 'Shadow', 'Luna', 'Smokey']


def create_sample_data(num_cats=10, num_missions=5):
    """Create random SpaceCats and Missions. Returns (cats, missions).

    Shared by the create_test_data management command and the
    create-test-data HTTP endpoint, so both build test data the same way.
    """
    cats = []
    for _ in range(num_cats):
        cats.append(SpaceCat.objects.create(
            name=random.choice(NAMES),
            role=random.choice(ROLES),
            age=random.randint(1, 20),
            mission_count=random.randint(0, 5),
        ))

    missions = []
    for _ in range(num_missions):
        mission = Mission.objects.create(
            name=f"Mission {random.randint(1, 100)}",
            description="A mission to explore the unknown regions of space.",
            launch_date=datetime.date.today() - datetime.timedelta(days=random.randint(0, 365)),
        )
        mission.spacecats.set(SpaceCat.objects.order_by('?')[:3])
        missions.append(mission)

    return cats, missions


def delete_sample_data():
    """Delete all SpaceCats and Missions. Returns (cats_deleted, missions_deleted).

    Shared by the delete_test_data management command and the
    delete-test-data HTTP endpoint, the mirror of create_sample_data.
    """
    cats_deleted = SpaceCat.objects.count()
    missions_deleted = Mission.objects.count()
    SpaceCat.objects.all().delete()
    Mission.objects.all().delete()
    return cats_deleted, missions_deleted
