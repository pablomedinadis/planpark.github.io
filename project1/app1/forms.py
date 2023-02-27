from .models import user
from django.contrib.auth import models
from django.forms import ModelForm
class userForm(ModelForm):
    class Meta:
        model=user
        fields='__all__'
