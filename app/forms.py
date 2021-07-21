from django import forms
#from leaflet.forms.widgets import LeafletWidget
from .models import *
#from .settings_models import *
#from django_select2.forms import ModelSelect2Widget, ModelSelect2MultipleWidget, ModelSelect2Mixin
#from django.utils.translation import gettext_lazy as _

class WorkerForm(forms.ModelForm):

    class Meta:
        model = WorkerModel
        exclude = ("id",)
        widgets = {
            
            'name':forms.TextInput(attrs={'class': 'form-control'}),
            'surname1' : forms.TextInput(attrs={'class': 'form-control'}),
            'surname2' : forms.TextInput(attrs={'class': 'form-control'}),
            'identification':forms.TextInput(attrs={'class': 'form-control'}),
            'birthday_date' :forms.DateInput(attrs={'class': 'form-control datepicker', 'autocomplete': 'off'}),

            'type' :forms.Select(attrs={'class': 'form-control'}),
            'is_social_service': forms.CheckboxInput(attrs={'class': 'form-control i-checks'}),
            }