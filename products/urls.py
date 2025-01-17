from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<item_id>', views.product_details, name='product_detail'),
    
]
