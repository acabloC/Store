from django.urls import path
from .views import products
app_name="product"

urlpatterns=[
    path("",products,name="index"),
    path('baskets/add/<int:product_id>/',basket_add, name = 'basket_add'),
]

