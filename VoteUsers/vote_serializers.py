__author__ = 'AVAndriets'

from VoteUsers.models import Vote
from rest_framework import serializers

class VoteSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username',        required=False)
    user_id = serializers.ReadOnlyField(source='user.id',               required=False)

    class Meta:
        model = Vote
        fields = ('id', 'comment', 'pollution_mark', 'vote_yes', 'vote_no', 'created_at', 'updated_at', 'user_id', 'username')

    def create(self, validated_data):
        vote = super(VoteSerializer, self).create(validated_data)
        vote.user = self.context['request'].user
        vote.save()

        return vote
