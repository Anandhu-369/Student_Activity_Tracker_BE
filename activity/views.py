from django.shortcuts import render
from django.db.models import Count, Sum
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Activity
from .serializers import ActivitySerializer
# Create your views here.


@api_view(["GET", "POST"])
def activity_list(request):
    if request.method == "POST":
        serializer = ActivitySerializer(data=request.data)

        if serializer.is_valid():
            activity = serializer.save()

            return Response(
                ActivitySerializer(activity).data,
                status=status.HTTP_201_CREATED,
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )

   
    activities = Activity.objects.all().order_by("-created_at")
    serializer = ActivitySerializer(activities, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def activity_summary(request):

    total_entries = Activity.objects.count()

    
    total_hours = (
        Activity.objects.aggregate(total=Sum("hours"))["total"] or 0
    )

  
    most_active = (
        Activity.objects.values("name")
        .annotate(total_hours=Sum("hours"), entries=Count("id"))
        .order_by("-total_hours", "name")
        .first()
    )

    return Response(
        {
            "total_entries": total_entries,
            "total_hours": total_hours,
            "most_active_user": (
                most_active["name"] if most_active else None
            ),
        },
        status=status.HTTP_200_OK,
    )