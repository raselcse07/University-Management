from django import forms
from Academic.models import Department



YEAR=[tuple([x,x]) for x in range(2008,2065)]



class ResultForm(forms.Form):

	Reg_No      =forms.CharField(label="Registration Number")
	Dept_name   =forms.ModelChoiceField(queryset=Department.objects.all(),empty_label="Select One")
	year 		=forms.CharField(label='Year',widget=forms.Select(choices=YEAR))
	secret_key	=forms.CharField(label='Secret Key')


class StudentLoginForm(forms.Form):

	Reg_No      =forms.CharField(label="Registration Number")
	secret_key	=forms.CharField(label='Secret Key')



