from django import forms
from .models import Kitob


class TalabaForm(forms.Form):
    ism = forms.CharField()
    kitoblar_soni = forms.IntegerField()
    kurs = forms.IntegerField()

