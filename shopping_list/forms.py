from django import forms
from .models import ItemList, User

#review the purpose of this method
# class PostForm(forms.Form):
#     content = forms.CharField(max_length=40)
    # value = forms.IntegerField()

# creating a form directly from the model that I built

class PostForm(forms.ModelForm):
    #here I am specifying the name of the model that I am using
    class Meta:
        model =  ItemList
        fields = ['item']
        # fields = "__all__"

# class UserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = '__all__'