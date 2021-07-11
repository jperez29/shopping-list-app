from django import forms
from .models import ItemList, User


class PostForm(forms.ModelForm):
    #here I am specifying the name of the model that I am using
    class Meta:
        model =  ItemList
        fields = ['item']
