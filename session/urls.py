from django.urls import path, include # Include is used to include other URLconfs
from .views import *

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('testsession/', testsession, name='testsession')
]