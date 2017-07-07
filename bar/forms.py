from django import forms
from .models import *


import datetime
class OrderForm(forms.ModelForm):
    date = forms.DateField(initial=datetime.date.today().strftime('%Y-%m-%d'), widget=forms.DateInput(attrs={'readonly': 'readonly',  'id':'datepicker',},))

    class Meta:
        model = Order
        widgets = {
            'table': forms.TextInput(attrs={'id':'table_id', 'type': 'hidden'}),
            'name': forms.TextInput(attrs={'placeholder': 'Ваше имя'}),
            'email': forms.TextInput(attrs={'placeholder': 'Ваш email'}),
        }
        fields = ['date', 'name', 'email', 'table']