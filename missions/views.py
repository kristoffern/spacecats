import logging
from django.http import HttpResponse
from missions.models import SpaceCat, Mission

# Configure logging
logger = logging.getLogger(__name__)

def index(request):
    logger.info('Index view called')
    try:
        spacecats = SpaceCat.objects.all()
        missions = Mission.objects.all()
        logger.debug(f'{spacecats.count()} spacecats found')
        logger.debug(f'{missions.count()} missions found')
        return HttpResponse("Check the logs for more details!")
    except Exception as e:
        logger.error(f'An error occurred: {e}')
        return HttpResponse("An error occurred, check the logs!")
