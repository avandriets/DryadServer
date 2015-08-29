from Vote.models import Vote
from Vote.vote_serializers import VoteSerializer
from rest_framework import filters
from rest_framework import viewsets


class VoteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Vote.objects.all()
    serializer_class = VoteSerializer

    filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter,)
    filter_fields = ('user', 'pollution_mark', )
    ordering_fields = ('created_at', 'updated_at', )
