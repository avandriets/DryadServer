from PicturesOfObjects.models import PicturesOfObjects
from rest_framework import serializers

__author__ = 'AVAndriets'


class PicturesOfObjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PicturesOfObjects
        fields = ('id', 'full_photoURL', 'pollution_mark', 'created_at', 'updated_at')
