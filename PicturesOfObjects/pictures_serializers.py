from PicturesOfObjects.models import PicturesOfObjects
from rest_framework import serializers

__author__ = 'AVAndriets'

class PicturesOfObjectsSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = PicturesOfObjects
        fields = ('id', 'full_photoURL', 'created_at', 'updated_at')

    # def create(self, validated_data):
    #     mark = super(PicturesOfObjectsSerializer, self).create(validated_data)
    #     mark.user = self.context['request'].user
    #     mark.save()
    #
    #     return mark