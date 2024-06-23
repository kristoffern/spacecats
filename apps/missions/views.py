import logging
from django.http import HttpResponse
from django.core.management import call_command

logger = logging.getLogger(__name__)

def create_test_data_view(request):
    try:
        call_command('create_test_data')
        return HttpResponse("Test data created successfully.")
    except Exception as e:
        logger.error(f"Error creating test data: {e}")
        return HttpResponse(f"Error creating test data: {e}", status=500)
