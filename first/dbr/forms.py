from django import forms
from django.contrib.auth.models import User
from dbr.models import UserProfile,DbaRoaster
from django.forms.widgets import DateInput


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('first_name','last_name','username','email','password')


class DateForm(forms.ModelForm):

    class Meta():
        model = DbaRoaster
        fields = ('date',)
        widgets = {
            'date': DateInput(attrs={'type': 'date'})
        }
