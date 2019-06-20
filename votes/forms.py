from django import forms
from .models import County, Category, Candidate


class CountyForm(forms.ModelForm):
    county_name = forms.ModelChoiceField(queryset=County.objects.all())

    class Meta:
        model = Candidate
        fields = ['county_name']
