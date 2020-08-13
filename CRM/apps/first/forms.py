from django.core.exceptions import ValidationError

from django import forms

from .models import Record


class RecordForm(forms.ModelForm):

    class Meta:
        model = Record
        fields = ('__all__')