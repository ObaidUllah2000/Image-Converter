from django import forms
from django.forms import fields
from django import forms
from home import models
from home.models import UploadImage

class UserImage(forms.ModelForm):
    class Meta:
        model = UploadImage
        fields = '__all__'