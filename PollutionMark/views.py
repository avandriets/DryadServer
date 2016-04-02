# coding=utf-8
from PollutionMark.models import PollutionMark
from PollutionMark.pollution_serializers import PollutionMarkSerializer
from gcm.models import get_device_model
from rest_framework import filters
from rest_framework import viewsets
import datetime
from rest_framework.renderers import JSONRenderer


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
            queryset = queryset.filter(updated_at__gt=datetime.datetime.fromtimestamp(long_value / 1e3))

        # return super(PollutionMarkViewSet, self).filter_queryset(queryset)
        return queryset

    def create(self, request, *args, **kwargs):
        created_object = super(PollutionMarkViewSet, self).create(request, *args, **kwargs)

        # point = PollutionMark.objects.get(pk=created_object.data['id'])
        # serializer = PollutionMarkSerializer(point)
        # array = [serializer.data]
        # content = JSONRenderer().render(array)

        device = get_device_model()
        device.objects.all().send_message({'NewPoint': created_object.data['id']})

        return created_object

    def destroy(self, request, *args, **kwargs):

        device = get_device_model()
        device.objects.all().send_message({'DeletePoint': kwargs['pk']})

        return super(PollutionMarkViewSet, self).destroy(request, *args, **kwargs)