from django import forms

# import datetime
# from django.utils import timezone
from .models import DaysAtWork
# from django.utils.dates import MONTHS

class DateTimeForm(forms.Form):
	date_time_input_1 = forms.DateField(widget=forms.DateInput(attrs = {'class':'form-control',}), input_formats=['%d/%m/%Y', '%d-%m-%Y'])
	date_time_input_2 = forms.TimeField(widget=forms.TimeInput(attrs = {'class':'form-control', 'placeholder':'start'}))
	date_time_input_3 = forms.TimeField(widget=forms.TimeInput(attrs = {'class':'form-control', 'placeholder':'finish'}))

class DateEditForm(forms.Form):
	date_time_input_4 = forms.DateField(widget=forms.DateInput(attrs = {'class':'form-control',}), input_formats=['%Y/%m'])

class DeleteForm(forms.Form):
    choices = forms.ModelMultipleChoiceField(
        queryset = DaysAtWork.objects.all(), # this is optional
        widget  = forms.CheckboxSelectMultiple,
    )



# '%Y/%m/%d', '%Y-%m',