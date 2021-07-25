from django import forms
#from leaflet.forms.widgets import LeafletWidget
from .models import *
#from .settings_models import *
#from django_select2.forms import ModelSelect2Widget, ModelSelect2MultipleWidget, ModelSelect2Mixin
#from django.utils.translation import gettext_lazy as _
from django_select2.forms import ModelSelect2Widget, ModelSelect2MultipleWidget, ModelSelect2Mixin
from django.utils.safestring import mark_safe

"""
class CustomCheckboxSelectMultiple(forms.CheckboxSelectMultiple):
    def render(self, name, value, attrs=None, renderer=None):
        html = super(CustomCheckboxSelectMultiple, self).render(name, value, attrs, renderer)
        html2 = html.replace('<ul id="id_categories" class="i-checks">', '<ul id="id_categories" class="four-columns">')
        return mark_safe(html2)

"""



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
            'identification_image_front': forms.FileInput(attrs={'accept': 'application/pdf, image/png, image/jpeg'}),
            
            'type' :forms.Select(attrs={'class': 'form-control'}),

            #'department' : ModelSelect2Widget(model=DepartmentModel, queryset=DepartmentModel.objects.filter(),
            #                                search_fields=['name__icontains'],
            #                                dependent_fields={'area': 'id'},
            #                                attrs={'style': 'width: 100%;'}),
            'department' : ModelSelect2Widget(model=DepartmentModel, queryset=DepartmentModel.objects.filter(),
                                            search_fields=['name__icontains'],
                                            attrs={'style': 'width: 100%;','data-placeholder':'Seleccionar'}),
            'is_social_service': forms.CheckboxInput(attrs={'class': 'form-control i-checks'}),
            'categories': forms.CheckboxSelectMultiple(attrs={'class': 'i-checks four-columns'}),
            }
"""
            members = forms.ModelMultipleChoiceField(
        queryset=Member.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    """