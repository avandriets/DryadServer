from django.contrib.auth.models import User
from rest_framework import serializers
 
 
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('password', 'first_name', 'last_name', 'email', 'username')
        write_only_fields = ('password',)
        read_only_fields = ('is_staff', 'is_superuser', 'is_active', 'date_joined',)

    def update(self, instance, validated_data):
        return super(UserSerializer, self).update(instance, validated_data)

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
