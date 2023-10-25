from django import forms
from .models import *

class TalabaForm(forms.Form):
    i = forms.CharField(label='Ism', max_length=30, min_length=3)
    k = forms.IntegerField(label="Kurs", max_value=7, min_value=1)
    k_s = forms.IntegerField(label="Kitoblar_soni")

class MuallifForm(forms.ModelForm):
    class Meta:
        model = Muallif
        fields = "__all__"

class KitobForm(forms.ModelForm):
    class Meta:
        model = Kitob
        fields = "__all__"

class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = '__all__'

class KutubxonachiForm(forms.Form):
    i = forms.CharField(label="Ism", max_length=30, min_length=3)
    ish = forms.TimeField(label="Ish vaqti")