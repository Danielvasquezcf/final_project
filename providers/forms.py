from django import forms

class ProviderForm(forms.Form):
    name = forms.CharField(max_length=100)
    address = forms.CharField(max_length=400)
    phone_number = forms.CharField(max_length=20)
    email = forms.EmailField()
    image = forms.ImageField()
    