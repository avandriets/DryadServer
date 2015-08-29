from PicturesOfObjects.pictures_serializers import PicturesOfObjectsSerializer
from PollutionMark.models import PollutionMark
from rest_framework import serializers

class PollutionMarkSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username',        required=False)
    user_id = serializers.ReadOnlyField(source='user.id',               required=False)
    first_name = serializers.ReadOnlyField(source='user.first_name',    required=False)
    last_name = serializers.ReadOnlyField(source='user.last_name',      required=False)
    pictures = PicturesOfObjectsSerializer(many=True, read_only=True,   required=False)
    vote_yes = serializers.IntegerField(source='vote.count', read_only=True)

    class Meta:
        model = PollutionMark
        fields = ('id', 'headline', 'full_description', 'longitude',
                  'latitude', 'attitude', 'created_at', 'updated_at',
                  'username','first_name', 'last_name',
                  'user_id', 'type', 'pictures', 'vote_yes')

    def create(self, validated_data):
        mark = super(PollutionMarkSerializer, self).create(validated_data)
        mark.user = self.context['request'].user
        mark.save()

        return mark
