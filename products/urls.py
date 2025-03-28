from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:item_id>', views.product_details, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
]
