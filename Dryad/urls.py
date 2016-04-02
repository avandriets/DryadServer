"""Dryad URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from PollutionMark.views import PollutionMarkViewSet
from PicturesOfObjects.views import PicturesOfObjectsViewSet
from VoteUsers.views import VoteViewSet
import apiusr.views
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'PollutionMark', PollutionMarkViewSet)
router.register(r'PicturesOfObjects', PicturesOfObjectsViewSet)
router.register(r'Vote', VoteViewSet)
router.register(r'accounts', apiusr.views.UserView, 'list')


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^rest/', include(router.urls)),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^auth/', include('rest_framework_social_oauth2.urls')),
    url(r'', include('gcm.urls')),
    #url(r'^api/', include(router.urls)),
]
