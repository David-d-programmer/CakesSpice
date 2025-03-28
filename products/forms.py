from django import forms
from .models import Product, Category



class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        
        # Change here: Use c.name instead of c.get_friendly_name()
        friendly_names = [(c.id, c.name) for c in categories]  # Assuming 'name' is the field

        self.fields['category'].choices = friendly_names
        
        # Add classes to all form fields
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
