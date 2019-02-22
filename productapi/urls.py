from django.urls import path, re_path
from . import views

app_name = "products"

urlpatterns = [
    path('<str:product_search>', views.ProductView, name='product'),
    path('other-products/<str:product_search>', views.ProductsView, name='products_brand'),
    path('product_not_found', views.ProductNotFoundView.as_view(), name='product_not_found'),
]