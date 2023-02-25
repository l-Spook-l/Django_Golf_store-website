from django.urls import path
from .views import StoreHome, TypeShow, BrandShow, ProductShow, AddProduct, UpdateProduct, DeleteProduct, ProfileUser

urlpatterns = [
    path('', StoreHome.as_view(), name='store_home'),
    path('t/<slug:type_slug>/', TypeShow.as_view(), name='type'),
    path('b/<slug:brand_slug>/', BrandShow.as_view(), name='brand'),
    path('p/<slug:product_slug>/', ProductShow.as_view(), name='product'),
    path('add-product/', AddProduct.as_view(), name='add_product'),
    path('update-product/<slug:product_slug>/', UpdateProduct.as_view(), name='update_product'),
    path('delete-product/<slug:product_slug>/', DeleteProduct.as_view(), name='delete_product'),
    path('profile/', ProfileUser.as_view(), name='profile'),
]
