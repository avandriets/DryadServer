from PollutionMark.models import PollutionMark
from PollutionMark.pollution_serializers import PollutionMarkSerializer
from VoteUsers.models import Vote
from VoteUsers.vote_serializers import VoteSerializer
from gcm.models import get_device_model
from rest_framework import filters
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer


class VoteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Vote.objects.all()
    serializer_class = VoteSerializer

    filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter,)
    filter_fields = ('user', 'pollution_mark', )
    ordering_fields = ('created_at', 'updated_at', )

    def create(self, request, *args, **kwargs):
        created_object = super(VoteViewSet, self).create(request, *args, **kwargs)

        # point = PollutionMark.objects.get(pk=created_object.data['pollution_mark'])
        # serializer = PollutionMarkSerializer(point)
        # array = [serializer.data]
        # content = JSONRenderer().render(array)

        device = get_device_model()
        device.objects.all().send_message({'NewMessage': created_object.data['pollution_mark']})

        return created_object
