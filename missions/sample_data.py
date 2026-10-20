import datetime
import random

from missions.models import Mission
from spacecats.models import SpaceCat

ROLES = ['Tester', 'Developer', 'Manager', 'Project Lead']

NAMES = [
    'Fluffy', 'Whiskers', 'Shadow', 'Luna', 'Smokey', 'Mochi', 'Pixel', 'Comet',
    'Nova', 'Biscuit', 'Mittens', 'Jynx', 'Pepper', 'Ziggy', 'Clover', 'Onyx',
    'Freya', 'Loki', 'Dusty', 'Hazel', 'Marbles', 'Binx', 'Gizmo', 'Saffron',
    'Tango', 'Willow', 'Cosmo', 'Orbit', 'Pumpkin', 'Sable', 'Juniper', 'Maple',
    'Pickle', 'Thistle', 'Rocket', 'Nimbus', 'Echo', 'Cinder', 'Basil', 'Suki',
]

MISSION_NAMES = [
    'Operation Stardust', 'The Kepler Run', 'Deep Field Survey', 'Nebula Drift',
    'The Long Dark', "Pilgrim's Reach", 'Red Horizon', 'Silent Transit',
    'The Oort Expedition', 'Halo Jump', 'Perihelion', 'The Vega Contact',
    'Dust Lane Recon', 'Cold Start', 'The Titan Ferry', 'Gravity Well',
    'Blue Shift', 'The Lagrange Hold', 'Ashfall', 'Meridian Pass',
    'The Europa Dive', 'Solar Maximum', 'Dark Transit', 'The Cassini Loop',
    'Far Anchor', 'Ion Tide', 'The Proxima Signal', 'Event Horizon',
    'Starfall', 'The Ceres Haul',
]

MISSION_DESCRIPTIONS = [
    'Chart the debris field beyond the fifth moon and map safe transit lanes.',
    'Escort a survey drone through the asteroid belt and recover its core samples.',
    'Investigate the cold signal drifting out past the heliopause.',
    'Resupply the forward station before the next solar storm hits.',
    'Map the magnetic anomaly reported near the ringed giant.',
    'Shadow the comet through perihelion and sample its tail.',
    'Re-establish contact with the silent relay on the ice moon.',
    'Tow the derelict freighter clear of the gravity well.',
    'Catalogue the newborn stars forming in the blue nebula.',
    'Run a deep-field sweep for anything the long-range sensors missed.',
    'Plant a beacon at the Lagrange point and hold position.',
    'Recover the lost probe from the edge of the dust lane.',
    'Survey the volcanic world for a stable landing site.',
    'Thread the binary system and log the tidal readings.',
    'Ferry the research team out to the outer canyon colony.',
    'Trace the aurora back to its source across the dark hemisphere.',
    'Scout a passage through the protoplanetary disk.',
    'Stand watch over the mining claim until relief arrives.',
]

NUM_CAT_IMAGES = 25
NUM_MISSION_IMAGES = 25


def _pick(pool, n):
    """n distinct entries when the pool allows, otherwise fall back to repeats."""
    return random.sample(pool, n) if n <= len(pool) else random.choices(pool, k=n)


def create_sample_data(num_cats=10, num_missions=5):
    """Create random SpaceCats and Missions. Returns (cats, missions).

    Shared by the create_test_data management command and the create-test-data HTTP
    endpoint. Names and descriptions are drawn without replacement so a single batch
    does not repeat. Each object is randomly assigned one of the fixed image pool;
    the template falls back to a placeholder when the image file is absent.
    """
    cat_names = _pick(NAMES, num_cats)
    mission_names = _pick(MISSION_NAMES, num_missions)
    mission_descriptions = _pick(MISSION_DESCRIPTIONS, num_missions)

    cats = []
    for name in cat_names:
        cats.append(SpaceCat.objects.create(
            name=name,
            role=random.choice(ROLES),
            age=random.randint(1, 20),
            mission_count=random.randint(0, 5),
            image=f"cat-{random.randint(1, NUM_CAT_IMAGES):02d}.png",
        ))

    missions = []
    for name, description in zip(mission_names, mission_descriptions):
        mission = Mission.objects.create(
            name=name,
            description=description,
            launch_date=datetime.date.today() - datetime.timedelta(days=random.randint(0, 365)),
            image=f"mission-{random.randint(1, NUM_MISSION_IMAGES):02d}.png",
        )
        mission.spacecats.set(SpaceCat.objects.order_by('?')[:3])
        missions.append(mission)

    return cats, missions


def delete_sample_data():
    """Delete all SpaceCats and Missions. Returns (cats_deleted, missions_deleted)."""
    cats_deleted = SpaceCat.objects.count()
    missions_deleted = Mission.objects.count()
    SpaceCat.objects.all().delete()
    Mission.objects.all().delete()
    return cats_deleted, missions_deleted
