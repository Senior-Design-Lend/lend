from django.urls import path, include
from transaction import views

app_name = 'transaction'

urlpatterns = [
    path('', views.listTransactionView.as_view(), name="list"),
    path('transactionList', views.listTransactionView.as_view(), name='list'),
    path('requestForm/<int:pk>/', views.createRequestView.as_view(), name='request'),
    path('requestList', views.listRequestView.as_view(), name='requestList'),
    path('requestDetail/<int:pk>', views.detailRequestView.as_view(), name='requestDetail'),
    path('transactionForm/<int:pk>/', views.createTransactionView.as_view(), name='transactionForm'),
    path('transactionDetail/<int:pk>', views.detailTransactionView.as_view(), name='transactionDetail'),


]
