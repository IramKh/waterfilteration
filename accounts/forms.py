from django.db.models import fields
from django.forms import ModelForm
from . models import *

class CustomerUpdateForm(ModelForm):
    class Meta:
        model = mukarram
        fields = '__all__'

