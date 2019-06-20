from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from votes.models import County, Category
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    county_name = forms.ModelChoiceField(queryset=County.objects.all())
    post = forms.ModelChoiceField(queryset=Category.objects.all())

    class Meta:
        model = User
        fields = ['username', 'email', 'county_name', 'post', 'password1','password2']

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)

        self.fields['username'].help_text = ''
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''



class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', ]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
