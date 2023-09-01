from django import forms
from .models import *

class AddProductForm(forms.Form):
    name = forms.CharField(max_length=255, label="Название продукта")
    photo = forms.ImageField()
    description = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}), label="Описание")
    price = forms.DecimalField(max_digits=10, decimal_places=2)
    quantity = price = forms.DecimalField(max_digits=10, decimal_places=2)


class ProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # super(ProductForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input'}),
            'description': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }