from django import forms
from django.forms import ModelForm
from .models import Product,Category
from users.models import Order

class AddProductForm(ModelForm):
    class Meta:
        model=Product
        fields='__all__'

    def __init__(self,*args,**kwargs):
        super(AddProductForm,self).__init__(*args,**kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})


class UpdateOrderForm(ModelForm):
    class Meta:
        model=Order
        fields=['status','in_cart']

    def __init__(self,*args,**kwargs):
        super(UpdateOrderForm,self).__init__(*args,**kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})
