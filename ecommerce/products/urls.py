from django.urls import path , include
from . import views



urlpatterns = [
   path('',views.products, name='products'),
   path('products/',views.product, name='product'),
]