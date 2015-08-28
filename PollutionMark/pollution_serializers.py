from PicturesOfObjects.pictures_serializers import PicturesOfObjectsSerializer
from PollutionMark.models import PollutionMark
from rest_framework import filters
from rest_framework import serializers


class PollutionMarkSerializer(serializers.HyperlinkedModelSerializer):
    username = serializers.ReadOnlyField(source='user.username',        required=False)
    user_id = serializers.ReadOnlyField(source='user.id',               required=False)
    first_name = serializers.ReadOnlyField(source='user.first_name',    required=False)
    last_name = serializers.ReadOnlyField(source='user.last_name',      required=False)
    pictures = PicturesOfObjectsSerializer(many=True, read_only=True)

    class Meta:
        model = PollutionMark
        fields = ('id', 'headline', 'full_description', 'full_photoURL', 'longitude', 'latitude', 'attitude', 'created_at', 'updated_at', 'username','first_name', 'last_name', 'user_id', 'type', 'pictures')

    filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter,)
    filter_fields = ('type', )
    ordering_fields = ('created_at', 'updated_at')

    def create(self, validated_data):
        mark = super(PollutionMarkSerializer, self).create(validated_data)
        mark.user = self.context['request'].user
        mark.save()

        return mark

