from django.urls import path
from . import views

urlpatterns = [
    path('', views.index2, name='index2'),
    path('products/', views.products, name='products'),
    path('product/', views.product, name='product'),
]