from django import forms
from Academic.models import Department






class TeacherList(forms.Form):

	Dept_name   =forms.ModelChoiceField(queryset=Department.objects.all(),empty_label="Select One")



class TeacherLogin(forms.Form):

	email	= forms.CharField(label="Email Address")
	secret_key	=forms.CharField(label='Secret Key')

