from PollutionMark.models import PollutionMark
from PollutionMark.pollution_serializers import PollutionMarkSerializer
from rest_framework import filters
from rest_framework import viewsets


class PollutionMarkViewSet(viewsets.ModelViewSet):

    queryset = PollutionMark.objects.all()
    serializer_class = PollutionMarkSerializer

    filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter,)
    filter_fields = ('type', )
    ordering_fields = ('created_at', 'updated_at')
