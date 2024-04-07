from django.urls import path
from .views import *
app_name="product"

urlpatterns=[
    path("",products,name="index"),
    path('basket/add/<int:product_id>/',basket_add, name = 'basket_add'),
    path('baskets/remove/<int:basket_id>/', basket_remove, name = 'basket_remove')
]

