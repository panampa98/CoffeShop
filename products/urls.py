from django.urls import path
from products.views import ProductFormView

urlpatterns = [
    path('add/', ProductFormView.as_view(), name='add_product'),
]