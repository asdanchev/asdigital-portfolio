from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=120, label="Your name")
    email = forms.EmailField(max_length=254, label="Your email")
    message = forms.CharField(label="What do you need?", widget=forms.Textarea)
