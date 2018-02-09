from django import forms
from django.forms import ModelForm
from .models import Register


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=60)
    email = forms.EmailField(label='Your email address', required=True)
    message = forms.CharField(widget=forms.Textarea)

class RegistrationForm(ModelForm):
    required_css_class = 'required'
    class Meta:
        model = Register
        fields = [
            'stu_name', 'date_of_birth', 'stu_address',
            'city', 'par_name', 'par_address', 'home_telephone',
            'place_employment', 'work_telephone', 'occupation',
            'email', 'par_name2', 'par_address2', 'home_telephone2',
            'place_employment2', 'work_telephone2', 'occupation2',
            'email2'
        ]