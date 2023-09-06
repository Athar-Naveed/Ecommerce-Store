from django import forms
from .models import Item

INPUT_CLASSES = 'w-full py-2 px-2 rounded-xl border-2'
class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category','name','description','price','image')

    def __init__(self,*args, **kwargs):
        super(NewItemForm,self).__init__(*args,**kwargs)

        self.fields['category'].widget.attrs['class'] = INPUT_CLASSES
        
        self.fields['name'].widget.attrs['class'] = INPUT_CLASSES
        self.fields['name'].widget.attrs['placeholder'] = "Product Name..."
        
        self.fields['description'].widget.attrs['class'] = INPUT_CLASSES
        self.fields['description'].widget.attrs['placeholder'] = "Product Description..."
        
        self.fields['price'].widget.attrs['class'] = INPUT_CLASSES
        self.fields['price'].widget.attrs['placeholder'] = "Product Price..."

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category','name','description','price','image','is_sold')

    def __init__(self,*args, **kwargs):
        super(EditItemForm,self).__init__(*args,**kwargs)
        self.fields['category'].widget.attrs['class'] = INPUT_CLASSES
        
        self.fields['name'].widget.attrs['class'] = INPUT_CLASSES
        self.fields['name'].widget.attrs['placeholder'] = "Product Name..."
        
        self.fields['description'].widget.attrs['class'] = INPUT_CLASSES
        self.fields['description'].widget.attrs['placeholder'] = "Product Description..."
        
        self.fields['price'].widget.attrs['class'] = INPUT_CLASSES
        self.fields['price'].widget.attrs['placeholder'] = "Product Price..."