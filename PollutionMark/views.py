from PollutionMark.models import PollutionMark
from PollutionMark.pollution_serializers import PollutionMarkSerializer
from django.shortcuts import render
from rest_framework import viewsets


class PollutionMarkViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    # obj.user = self.request.user
    queryset = PollutionMark.objects.all()
    serializer_class = PollutionMarkSerializer

    def perform_create(self, serializer):
        #serializer.context['request'].data.pop('user',self.request.user)
        #serializer.data['user'] = self.request.user
        #serializer.save(user=self.request.user)
        super(PollutionMarkViewSet, self).perform_create(serializer)

