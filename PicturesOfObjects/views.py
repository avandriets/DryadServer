from PicturesOfObjects.models import PicturesOfObjects
from PicturesOfObjects.pictures_serializers import PicturesOfObjectsSerializer
from PollutionMark.models import PollutionMark
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets


class PicturesOfObjectsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = PicturesOfObjects.objects.all()
    serializer_class = PicturesOfObjectsSerializer
