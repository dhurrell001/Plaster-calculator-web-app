# your_app_name/forms.py

from django import forms
from .models import Plaster


class PlasterCalculatorForm(forms.Form):
    radio_choices = [
        ('external', 'External'),
        ('internal', 'Internal'),
    ]
    Area_of_use = forms.ChoiceField(
        choices=radio_choices,
        widget=forms.RadioSelect(attrs={'class': 'radio-inline'}),
        label="Area of Use"
    )

    plasterType = forms.ModelChoiceField(
        queryset=Plaster.objects.all(), empty_label="Select a plaster", label="Plaster Type")
    length = forms.DecimalField(label="Please enter length in metres")
    width = forms.DecimalField(label="Please enter length in metres")
    thickness = forms.DecimalField(
        label="Please enter plaster thickness in MM")
    contingency = forms.DecimalField(label="Please enter contigency in %")


class PlasterResultForm(forms.Form):

    total_area = forms.DecimalField(
        label="Total area in square metres",
        required=False,
        widget=forms.TextInput(attrs={'readonly': 'readonly'})
    )

    plaster_amount = forms.DecimalField(
        label="Plaster Amount Needed in KG",
        required=False,
        widget=forms.TextInput(attrs={'readonly': 'readonly'})
    )

    bags_needed = forms.DecimalField(
        label="Bags Needed",
        required=False,
        widget=forms.TextInput(attrs={'readonly': 'readonly'})
    )
