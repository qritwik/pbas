from django import forms
from .models import *
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.forms import modelformset_factory

class LoginForm(AuthenticationForm):
	'''
	Form for taking Username and password
	'''
	username = forms.CharField(label="usn", max_length=30,
							   widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username', 'id': 'username','placeholder': 'Enter Username'}))
	password = forms.CharField(label="Password", max_length=30,
							   widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'otp', 'id': 'otp', 'placeholder': 'Enter OTP'}))

class form_conference(forms.ModelForm):
	class Meta:
		model = conference
		fields = '__all__'
		exclude = ['info']



class form_journal(forms.ModelForm):
	class Meta:
		model = journal
		fields = '__all__'
		exclude = ['info']


class form_User(forms.ModelForm):

	class Meta:
		model = User
		fields = '__all__'




class form_empDetailForm(forms.ModelForm):

	class Meta:
		model = empDetailForm
		fields = '__all__'
		exclude = ['info']


class form_feedbackTab(forms.ModelForm):

	class Meta:
		model = feedbackTab
		fields = '__all__'
		exclude = ['info']




class form_rd(forms.ModelForm):

	class Meta:
		model = rd
		fields = '__all__'
		exclude = ['info']



class form_remarks(forms.ModelForm):

	class Meta:
		model = remarks
		fields = '__all__'
		exclude = ['info']

class form_remarks1(forms.ModelForm):

	class Meta:
		model = remarks1
		fields = '__all__'
		exclude = ['info']

class form_remarks2(forms.ModelForm):

	class Meta:
		model = remarks2
		fields = '__all__'
		exclude = ['info','department']
