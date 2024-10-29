from django.urls import path
from .views import product_list, add_product, seller_product_list, edit_product

urlpatterns = [
    path('products/', product_list, name='product_list'),
    path('my_products/', seller_product_list, name='my_product_list'),
    path('add/', add_product, name='add_product'),
    path('edit/<str:product_id>/', edit_product, name='edit_product'),
]
