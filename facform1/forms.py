from django import forms
from .models import *
from django.contrib.auth.forms import AuthenticationForm
from django import forms

class LoginForm(AuthenticationForm):
	'''
	Form for taking Username and password
	'''
	username = forms.CharField(label="usn", max_length=30,
							   widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username', 'id': 'username','placeholder': 'Enter Username'}))
	password = forms.CharField(label="Password", max_length=30,
							   widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'otp', 'id': 'otp', 'placeholder': 'Enter OTP'}))



class form_empDetailForm(forms.ModelForm):

	class Meta:
		model = empDetailForm
		fields = '__all__'
		exclude = ['emp_id']



class form_feedbackTab(forms.ModelForm):

	class Meta:
		model = feedbackTab
		fields = '__all__'
		exclude = ['emp_id']




class form_rd(forms.ModelForm):

	class Meta:
		model = rd
		fields = '__all__'
		exclude = ['emp_id']



class form_remarks(forms.ModelForm):

	class Meta:
		model = remarks
		fields = '__all__'
		exclude = ['emp_id']