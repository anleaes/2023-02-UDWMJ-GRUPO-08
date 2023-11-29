from django import forms
from .models import item

class ItemForm(forms.ModelForm):

    class Meta:
        model = item
        exclude = ('created_on' , 'updated_on',)