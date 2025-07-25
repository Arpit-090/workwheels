from django.urls import path
from . import views

urlpatterns=[
    path('',views.authhome,name="authhome"),
    path('/login',views.login,name="authhome"),
]