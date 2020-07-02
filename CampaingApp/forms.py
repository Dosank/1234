from django import forms

from .models import Campaing, User

class CreateCampaingF(forms.ModelForm):
    class Meta:
        model = Campaing
        fields = ("title", "master")