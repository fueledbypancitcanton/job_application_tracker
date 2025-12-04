from django import forms
from .models import Job

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'
        widgets = {
            "date_applied": forms.DateInput(attrs={"type": "date"})
        }