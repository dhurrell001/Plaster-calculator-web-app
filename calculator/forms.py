# your_app_name/forms.py

from django import forms
from .models import Plaster


class PlasterCalculatorForm(forms.Form):
    plasterType = forms.ModelChoiceField(
        queryset=Plaster.objects.all(), empty_label="Select a plaster", label="Plaster Type")
    length = forms.DecimalField(label="Please enter length in metres")
    width = forms.DecimalField(label="Please enter length in metres")
