from django.urls import path
from django.urls import re_path as url
# from django.conf.urls import url
from .views import dashboard, profile_list, profile, imageAPI, textAPI

app_name = "dwitter"

urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("profile_list/", profile_list, name="profile_list"),
    path("profile/<int:pk>", profile, name="profile"),
    url('api/image', imageAPI, name='imageAPI'),
    url('api/text', textAPI, name='textAPI'),
]
