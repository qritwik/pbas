from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from . import forms
import urllib.parse as ap
import urllib.request
from django.contrib.auth.hashers import make_password, check_password



def phone_otp(random_otp, phone):
		phone1 = str(phone)
		message = 'Please login with the OTP: '+random_otp
		params = { 'number' : phone1, 'text' : message }
		baseUrl = 'https://www.smsgatewayhub.com/api/mt/SendSMS?APIKey=62sxGWT6MkCjDul6eNKejw&senderid=BMSITM&channel=2&DCS=0&flashsms=0&' + ap.urlencode(params)
		urllib.request.urlopen(baseUrl).read(1000)


def login(request):
	if(request.method=='POST'):

		username = request.POST.get('username')

		if(User.objects.filter(username=username).exists()):
			user = User.objects.get(username=username)
			first_name = user.first_name
			email = user.email
			phone = user.phone
			random_otp = '12345'
			phone_otp(random_otp,phone)

			hashed_pwd = make_password(random_otp)
			User.objects.filter(username=username).update(password=hashed_pwd)

			return HttpResponseRedirect("/login/user=" + username)

	return render(request,'login.html')

def decide_view(request):
	if request.user.is_assistant_professor():
		print('assis')
		return HttpResponseRedirect("/assistant_form/")

	elif request.user.is_associate_professor():
		print('asso')
		return HttpResponseRedirect("/associate_form/")

	elif request.user.is_hod():
		print('hod')
		return HttpResponseRedirect("/hod_first/")

	elif request.user.is_principal():
		print('princy')
		return HttpResponseRedirect("/principal_first/")

	elif request.user.is_ao():
		return HttpResponseRedirect("/ao.first/")

	else:
		return HttpResponseRedirect("/")
# def front(request):
# 	return render(request,'front.html')




def hod_form(request):
	return render(request,'hod_form.html')

def hod_display(request):
	return render(request,'hod_display.html')

def principal_display(request):
	return render(request,'principal_display.html')

def hod_first(request):
	return render(request,'hod_first.html')

def principal_first(request):
	return render(request,'principal_first.html')

def success(request):
	return render(request,'hod_success.html')

def f_assistant(request):

	form2 = forms.form_empDetailForm()
	form3 = forms.form_feedbackTab()
	form4 = forms.form_rd()

	if request.method == 'POST':
		if  form2.is_valid():
			form2.save()
			render(request,'hod_success.html')	

	return render(request,'assistant_form.html',{'form2':form2,'form3':form3,'form4':form4})

def f_associate(request):

	form2 = forms.form_empDetailForm()
	form3 = forms.form_feedbackTab()
	form4 = forms.form_rd()

	# if request.method == 'POST':
	# 	if form1.is_valid() and form2.is_valid() and form3.is_valid() and form4.is_valid():
	return render(request,'associate_form.html',{'form2':form2,'form3':form3,'form4':form4})


