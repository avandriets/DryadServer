# coding=utf-8
from apiusr.serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from .permissions import IsStaffOrTargetUser
 
 
class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    model = User
 
    def get_permissions(self):

        # allow non-authenticated user to create via POST
        return (IsAuthenticated() if self.request.method == 'POST' and self.request.user.username == 'mobile_user_manager' else IsStaffOrTargetUser()),