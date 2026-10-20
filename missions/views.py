import logging

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import DetailView, ListView

from missions.models import Mission
from missions.sample_data import create_sample_data, delete_sample_data

logger = logging.getLogger(__name__)


class MissionListView(ListView):
    model = Mission
    template_name = 'missions/mission_list.html'
    context_object_name = 'missions'

    def get(self, request, *args, **kwargs):
        logger.info("Mission list view called")
        logger.info(f"{Mission.objects.count()} Missions on the board")
        return super().get(request, *args, **kwargs)


class MissionDetailView(DetailView):
    model = Mission
    template_name = 'missions/mission_detail.html'
    context_object_name = 'mission'

    def get(self, request, *args, **kwargs):
        logger.info(f"Mission detail view called for pk={kwargs.get('pk')}")
        return super().get(request, *args, **kwargs)


def create_test_data_view(request):
    try:
        cats, missions = create_sample_data()
        logger.info(
            f"create-test-data endpoint created {len(cats)} SpaceCats "
            f"and {len(missions)} Missions"
        )
        return render(request, 'missions/test_data_created.html', {
            'cats': cats,
            'missions': missions,
        })
    except Exception as e:
        logger.error(f"Error creating test data: {e}")
        return HttpResponse(f"Error creating test data: {e}", status=500)


def delete_test_data_view(request):
    try:
        cats_deleted, missions_deleted = delete_sample_data()
        logger.info(
            f"delete-test-data endpoint removed {cats_deleted} SpaceCats "
            f"and {missions_deleted} Missions"
        )
        return render(request, 'missions/test_data_deleted.html', {
            'cats_deleted': cats_deleted,
            'missions_deleted': missions_deleted,
        })
    except Exception as e:
        logger.error(f"Error deleting test data: {e}")
        return HttpResponse(f"Error deleting test data: {e}", status=500)
