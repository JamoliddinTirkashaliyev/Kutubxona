from django import forms
from .models import *


class TalabaForm(forms.Form):
    ism = forms.CharField()
    kitoblar_soni = forms.IntegerField()
    kurs = forms.IntegerField()

class MuallifForm(forms.Form):
    ism = forms.CharField()
    jins = forms.CharField()
    tugulgan_sana = forms.DateField()
    tirik = forms.BooleanField()
    kitoblar_soni = forms.IntegerField()


class RecordForm(forms.ModelForm):
   class Meta:
       model = Record
       fields = '__all__'


class KutubxonachiForm(forms.ModelForm):
    class Meta:
        model = Kutubxonachi
        fields = '__all__'



