from django.urls import path
from .views import customer_list, add_customer, delete_customer

urlpatterns = [
    path('', customer_list, name='customers'),
    path('add/', add_customer, name='add_customer'),
    path('delete/<int:id>/', delete_customer, name='delete_customer'),
]