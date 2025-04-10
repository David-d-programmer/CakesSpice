from django.urls import path
from . import views

urlpatterns = [
    path('view_bag', views.view_bag, name='view_bag'),
    path('add_to_bag/<int:item_id>/', views.add_to_bag, name='add_to_bag'),
    path('adjust_bag/<int:item_id>/', views.adjust_bag, name='adjust_bag'),
    path('bag/remove/<int:item_id>/', views.remove_from_bag, name='remove_from_bag')

]
