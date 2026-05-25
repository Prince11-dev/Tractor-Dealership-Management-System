from django.urls import path
from .views import sales_list, add_sale

urlpatterns = [

    path('', sales_list, name='sales'),
    path('add/', add_sale, name='add_sale'),

]