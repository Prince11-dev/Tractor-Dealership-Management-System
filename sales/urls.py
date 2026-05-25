from django.urls import path
from .views import (
    sales_list,
    add_sale,
    update_sale,
    delete_sale
)

urlpatterns = [

    path('', sales_list, name='sales'),
    path('add/', add_sale, name='add_sale'),
    path('update/<int:id>/', update_sale, name='update_sale'),
    path('delete/<int:id>/', delete_sale, name='delete_sale'),

]