from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label='Name', required=True, widget=forms.TextInput(
        attrs={"class": "form-control"}
    ))
    email = forms.EmailField(label='Email', required=True, widget=forms.EmailInput(
        attrs={"class": "form-control", 'placeholder':'Writte an email'}
    ))
    content = forms.CharField(label='Message', required=True, widget=forms.Textarea(
        attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Writte a message'}
    ))
