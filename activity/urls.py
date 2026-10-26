from django.urls import path
from .views import activity_list, activity_summary

urlpatterns = [
    path("activities/", activity_list, name="activity-list"),
    path(
        "activities/summary/",
        activity_summary,
        name="activity-summary",
    ),
]