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
    # obj.user = self.request.user
    queryset = PicturesOfObjects.objects.all()
    serializer_class = PicturesOfObjectsSerializer

    def perform_create(self, serializer):
        #serializer.context['request'].data.pop('user',self.request.user)
        #serializer.data['user'] = self.request.user
        #serializer.save(user=self.request.user)
        super(PicturesOfObjectsViewSet, self).perform_create(serializer)