from django.urls import path

from helloworld import views

urlpatterns = [
    path('', views.users, name='users'),

]
