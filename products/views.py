from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView
from products.forms import ProductForm

# Create your views here.
class ProductFormView(FormView):
    template_name = 'products/add_product.html'
    form_class = ProductForm
    success_url = reverse_lazy('add_product')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)