from django import forms

#review the purpose of this method
class PostForm(forms.Form):
    content = forms.CharField(max_length=40)
    value = forms.IntegerField()