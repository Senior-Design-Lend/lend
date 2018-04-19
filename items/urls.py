from django.urls import path, include
from items import views

app_name = 'items'

urlpatterns = [
    path('', views.listItemView.as_view(), name="list"),
    path('<int:pk>/', views.detailItemView.as_view(), name="detail"),
    path('addItem', views.createItemView.as_view(),name="create"),
    path('update/<int:pk>/', views.updateItemView.as_view(), name="update"),
    path('delete/<int:pk>/', views.deleteItemView.as_view(), name="delete"),

]
