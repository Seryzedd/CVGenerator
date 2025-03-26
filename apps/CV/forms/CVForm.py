from dataclasses import replace
from django import forms
from django.forms import ModelForm
import os
from apps.login.utils.validator import validate_alpha
from apps.CV.models.CV import CV


def getTemplates():
    dir = os.path.abspath('apps/CV/templates/templatesFilesHTML')

    return ((file, file.replace('.html', ''))for file in os.listdir(dir))

class CvForm(forms.Form):
    name = forms.CharField(
        max_length=50,
        required=True,
        label='Nom du CV',
        validators=[validate_alpha],
        widget=forms.TextInput(
            attrs={
                'placeholder': '',
                'class': 'form-control text-center mb-2'
            }
        )
    )

    description = forms.CharField(
        max_length=255,
        required=False,
        label='Description du CV',
        widget=forms.Textarea(
            attrs={
                'placeholder': '',
                'class': 'form-control text-center mb-2',
                'rows' : "5"
            }
        )
    )

    template = forms.ChoiceField(
        required=True,
        label='template utilisé',
        choices=getTemplates(),
        widget=forms.Select(
            attrs={'class':'form-control text-center mb-2'},

        )
    )

    primaryColor = forms.CharField(
        max_length=100,
        required=True,
        label='Couleur primaire',
        widget=forms.TextInput(attrs={'type': 'color', 'class': 'form-control form-control-color'})
    )

    secondaryColor = forms.CharField(
        max_length=100,
        required=True,
        label='Couleur secondaire',
        widget=forms.TextInput(attrs={'type': 'color', 'class': 'form-control form-control-color'})
    )

    class Meta:
        model = CV
        fields = ["name", "description", "template", "primaryColor", "secondaryColor"]

    def setData(self, data):
        self.initial['name']=data.name
        self.initial['description'] = data.description
        self.initial['template'] = data.template
        self.initial['primaryColor'] = data.primaryColor
        self.initial['secondaryColor'] = data.secondaryColor


    def clean(self):
        return super().clean()