from django import forms
from products.models import Product

class ProductForm(forms.Form):
    name = forms.CharField(max_length=255, label='Name')
    description = forms.CharField(max_length=255, label='Description')
    price = forms.DecimalField(max_digits=10, decimal_places=2, label='Price')
    available = forms.BooleanField(initial=True, label='Available', required=False)
    image = forms.ImageField(label='Image', required=False)

    def save(self):
        data = self.cleaned_data
        product = Product.objects.create(
            name=data['name'],
            description=data['description'],
            price=data['price'],
            available=data['available'],
            image=data['image']
        )
        return product