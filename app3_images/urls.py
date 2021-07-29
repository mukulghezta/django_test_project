from django.urls import path
from .views import *

urlpatterns = [
    path('profile/', profile, name="profile"),
    path('create_profile/', create_profile, name="create_profile"),
]