from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from plants.views import PlantsView

urlpatterns = [
    path("plants", csrf_exempt(PlantsView.as_view()), name="plants"),
    path("plants/<int:id>", csrf_exempt(PlantsView.as_view()), name="plants_edit"),
]
