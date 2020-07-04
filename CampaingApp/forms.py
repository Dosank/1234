from django import forms

from .models import Campaing, User

# Forma de hacerlo
class CreateCampaingF(forms.ModelForm):
    class Meta:
        model = Campaing
        fields = ("title", "master")

# Otra forma de hacerlo
class CreateCampaingF2(forms.Form):
    title = forms.CharField()
    master = forms.ModelChoiceField(User.objects.all())