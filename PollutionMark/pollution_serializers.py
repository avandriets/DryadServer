from PollutionMark.models import PollutionMark
from rest_framework import serializers


class PollutionMarkSerializer(serializers.HyperlinkedModelSerializer):
    username = serializers.ReadOnlyField(source='user.username',        required=False)
    user_id = serializers.ReadOnlyField(source='user.id',        required=False)
    first_name = serializers.ReadOnlyField(source='user.first_name',    required=False)
    last_name = serializers.ReadOnlyField(source='user.last_name',      required=False)

    class Meta:
        model = PollutionMark
        fields = ('id', 'headline', 'full_description', 'full_photoURL', 'longitude', 'latitude', 'created_at', 'username','first_name', 'last_name', 'user_id')

    def create(self, validated_data):
        #user_data = validated_data.pop(u'user', self.context['request'].user)
        #,self.context['request'].user
        mark = super(PollutionMarkSerializer, self).create(validated_data)
        mark.user = self.context['request'].user
        mark.save()

        return mark

