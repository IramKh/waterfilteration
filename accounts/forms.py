from django.db.models import fields
from django.forms import ModelForm
from .models import *


class CustomerUpdateForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

class Product_Detail_form(ModelForm):
    class Meta:
        model = Our_Product
        fields = '__all__'

