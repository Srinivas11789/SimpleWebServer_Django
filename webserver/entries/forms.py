from django import forms
 
class FirstPage(forms.Form):
    entry = forms.CharField(max_length=100)
