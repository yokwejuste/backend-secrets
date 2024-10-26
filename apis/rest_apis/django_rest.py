# views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def api_root(request):
    return Response({"message": "Welcome to Django REST API!"})


# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_root, name='api_root'),
]
