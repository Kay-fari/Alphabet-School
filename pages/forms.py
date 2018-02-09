from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=60)
    email = forms.EmailField(label='Your email address', required=True)
    message = forms.CharField(widget=forms.Textarea)