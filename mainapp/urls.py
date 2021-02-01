from django.urls import path
from mainapp.views import products

urlpatterns = [
    path('',products,name='products'),
    path('<int:id>',products,name='product'),

               ]
