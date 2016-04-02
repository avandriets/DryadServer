from PicturesOfObjects.models import PicturesOfObjects
from PicturesOfObjects.pictures_serializers import PicturesOfObjectsSerializer
from PollutionMark.models import PollutionMark
from django.shortcuts import render

# Create your views here.
from gcm.models import get_device_model
from rest_framework import viewsets
from rest_framework.response import Response


class PicturesOfObjectsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = PicturesOfObjects.objects.all()
    serializer_class = PicturesOfObjectsSerializer

    def destroy(self, request, *args, **kwargs):

        device = get_device_model()
        device.objects.all().send_message({'DeletePicture':kwargs['pk']})

        return super(PicturesOfObjectsViewSet, self).destroy(request, *args, **kwargs)