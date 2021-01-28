from django import forms
from .models import Product, Category


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'

        self.fields['category'].choices = friendly_names
        self.fields['discount_price'].widget.attrs['required'] = False
        self.fields['discount_price'].widget.attrs['disabled'] = True
        self.fields['price'].widget.attrs['placeholder'] = "£"



