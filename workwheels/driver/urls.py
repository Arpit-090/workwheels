from django.urls import path
from . import views

urlpatterns=[
    path('driver/',views.driver_home,name="driver_home"),
]