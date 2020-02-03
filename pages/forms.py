from django import forms
from users.models import CustomUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class View_bioForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email')

