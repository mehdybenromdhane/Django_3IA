from django import forms
from .models import Conference

class ConferenceModelForm(forms.ModelForm):
    class Meta:
        model=Conference
        fields = '__all__'
        
        exclude=('reservation',)
    start_date=forms.DateField(
        label="Conference Start Date",
        widget=forms.DateInput(
            attrs={
                'type' : 'date',
                'style':'color:red;'
                
            }
        ))
    end_date=forms.DateField(
        label="Conference End Date",
        widget=forms.DateInput(
            attrs={
                'type' : 'date',
            }
        ))