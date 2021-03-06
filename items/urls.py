from django.urls import path, include
from items import views
from django.contrib.auth.decorators import login_required

app_name = 'items'

urlpatterns = [
    path('', views.listItemView.as_view(), name="list"),
    path('<int:pk>/', views.detailItemView.as_view(), name="detail"),
    path('addItem', login_required(views.createItemView.as_view()),name="create"),
    path('update/<int:pk>/', login_required(views.updateItemView.as_view()), name="update"),
    path('delete/<int:pk>/', login_required(views.deleteItemView.as_view()), name="delete"),
    path('itemList', views.listItemView.as_view(), name='list'),

]
