from django import forms
from .models import Inventory, Player, InventoryItem ,Item

class InventoryForm(forms.ModelForm):
    
    class Meta:
        model = Inventory
        exclude = ('player', 'created_on' , 'updated_on')

class InventoryItemForm(forms.ModelForm):
    
    class Meta:
        model = InventoryItem
        exclude = ('inventory', 'created_on' , 'updated_on')