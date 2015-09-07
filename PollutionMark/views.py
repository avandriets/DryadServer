# coding=utf-8
from PollutionMark.models import PollutionMark
from PollutionMark.pollution_serializers import PollutionMarkSerializer
from rest_framework import filters
from rest_framework import viewsets
import datetime

class PollutionMarkViewSet(viewsets.ModelViewSet):

    queryset = PollutionMark.objects.all()
    serializer_class = PollutionMarkSerializer

    filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter,)
    filter_fields = ('type', 'updated_at',)
    ordering_fields = ('created_at', 'updated_at')

    def filter_queryset(self, queryset):

        queryset = PollutionMark.objects.all()

        type_val = self.request.QUERY_PARAMS.get('type', None)
        updated_at_val = self.request.QUERY_PARAMS.get('updated_at', None)

        if type_val is not None:
            queryset = queryset.filter(type=type_val)

        if updated_at_val is not None:
            long_value = long(float(updated_at_val))
            queryset = queryset.filter(updated_at__gt=datetime.datetime.fromtimestamp(long_value/1e3))

        #return super(PollutionMarkViewSet, self).filter_queryset(queryset)
        return queryset
