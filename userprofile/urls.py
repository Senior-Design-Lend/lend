from django.urls import path, include
from userprofile import views

app_name = "profile"

urlpatterns = [
	path('',views.profileView.as_view(),name='profile'),
]
