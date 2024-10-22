# forms.py

from django import forms
from .models import About, Tarif, Event

class TarifForm(forms.ModelForm):
    class Meta:
        model = Tarif
        fields = ['formule', 'name', 'price', 'description']

class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = ['about_Julien','about_Chanth','about']

class ContactForm(forms.Form):
    name = forms.CharField(label='Votre nom', max_length=100)
    email = forms.EmailField(label='Votre Email')
    subject = forms.CharField(label='Sujet', max_length=100)
    message = forms.CharField(label='Message', widget=forms.Textarea)

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'start_time', 'end_time']
        
        widgets = {
            'start_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }