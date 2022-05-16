import email
from django import forms
from .models import Report


class ReportForm1(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['name','email','phone', 'description']



class ReportForm2(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['name','email','phone']
