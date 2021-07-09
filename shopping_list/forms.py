from django import forms
from .models import ItemList

#review the purpose of this method
# class PostForm(forms.Form):
#     content = forms.CharField(max_length=40)
    # value = forms.IntegerField()

# creating a form directly from the model that I built

class PostForm(forms.ModelForm):
    #here I am specifying the name of the model that I am using
    class Meta:
        model =  ItemList
        fields = "__all__"