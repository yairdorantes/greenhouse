from datetime import timedelta
import json
from django.utils import timezone
from django.http import JsonResponse
from django.views import View
from loguru import logger

from plants.models import Plants


def needs_watering(next_water) -> bool:
    try:
        if timezone.localtime().date() >= next_water:
            return True
        else:
            return False
    except Exception as e:
        print("An error occurred:", e)
        return False


# API VIEW DJANGO
class PlantsView(View):
    def get(self, request, id=0):
        logger.debug(f"getting watering info... at {timezone.localtime()}")
        try:
            plant = Plants.objects.filter(id=id).first()
            watering = needs_watering(plant.next_water)
            return JsonResponse({"needs_water": watering})
        except Exception as e:
            print("An error occurred:", e)
            return JsonResponse({"error": str(e)}, status=500)

    def post(self, request):
        try:
            Plants.objects.create(
                name="test",
                last_water=timezone.now(),
                next_water=timezone.now(),
            )
            return JsonResponse({"message": "Plant created"})
        except Exception as e:
            print("An error occurred:", e)
            return JsonResponse({"error": str(e)}, status=500)

    # plants/models.py
    def put(self, request, id=0):
        logger.debug(f"updating watering info... at {timezone.localtime()}")
        try:
            plant = Plants.objects.filter(id=id).first()
            print(plant)
            if not plant:
                return JsonResponse(
                    {"message": "Plant with the given ID does not exist"},
                    status=404,
                )
            # data = json.loads(request.body)
            # plant.name = data.get("name", plant.name)
            plant.last_water = timezone.now()
            plant.next_water = plant.next_water + timedelta(days=4)
            plant.save()
            return JsonResponse({"message": "Plant updated"}, status=200)
        except Exception as e:
            print("An error occurred:", e)
            return JsonResponse({"error": str(e)}, status=500)
