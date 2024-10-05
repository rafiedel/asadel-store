from django import forms
from django.forms import ModelForm
from main.models import Product
from django.utils.html import strip_tags

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description", "stock_available", "photo"]
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.error_messages = {
                'required': 'This field is required.',
                'invalid': 'Enter a valid value.',
                'invalid_choice': 'Select a valid choice. That choice is not one of the available choices.',
                'unique': 'This value must be unique.',
                'invalid_image': 'Upload a valid image. The file you uploaded was either not an image or a corrupted image.',
                'invalid_file': 'Upload a valid file. The file you uploaded was either not a valid file type or is corrupted.',
            }
    
    # def clean_name(self):
    #     name = self.cleaned_data['name']
    #     return strip_tags(name)
    
    # def clean_price(self):
    #     price = self.cleaned_data['price']
    #     return strip_tags(print)
    
    # def clean_description(self):
    #     description = self.cleaned_data['description']
    #     return strip_tags(description)
    
    # def clean_stock_available(self):
    #     stock_available = self.cleaned_data['stock_available']
    #     return strip_tags(stock_available)
    
    # def clean_photo(self):
    #     photo = self.cleaned_data['photo']
    #     return strip_tags(photo)
    