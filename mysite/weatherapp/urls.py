from django.urls import path


# the same as saying from weatherapp import views
from . import views 

urlpatterns = [
    path('', views.index)
]