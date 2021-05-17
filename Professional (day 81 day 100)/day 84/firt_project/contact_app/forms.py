from django import forms
from .models import ContactForm

class ContactForms(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['user', 'email', 'comment']