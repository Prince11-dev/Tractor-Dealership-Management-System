from django.urls import path
from .views import (
    tractor_list,
    add_tractor,
    update_tractor,
    delete_tractor
)

urlpatterns = [

    path('', tractor_list, name='tractors'),
    path('add/', add_tractor, name='add_tractor'),
    path('update/<int:id>/', update_tractor, name='update_tractor'),
    path('delete/<int:id>/', delete_tractor, name='delete_tractor'),

]