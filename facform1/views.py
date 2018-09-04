from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from . import forms
import urllib.parse as ap
import urllib.request


def phone_otp(random_otp, phone):
		'''
		Sends OTP to phone
		'''
		phone1 = str(phone)
		message = 'Please login with the OTP: '+random_otp
		params = { 'number' : phone1, 'text' : message }
		baseUrl = 'https://www.smsgatewayhub.com/api/mt/SendSMS?APIKey=62sxGWT6MkCjDul6eNKejw&senderid=BMSITM&channel=2&DCS=0&flashsms=0&' + ap.urlencode(params)
		urllib.request.urlopen(baseUrl).read(1000)


def login(request):
	if(request.method=='POST'):
		emp_id = request.POST.get('emp_id')
		if(empDetail.objects.filter(emp_id=username).exists()):

			first_name = empDetail.objects.filter(emp_id=emp_id).values('first_name')
			First_name = first_name[0]['first_name']
			email = empDetail.objects.filter(emp_id=emp_id).values('email')
			Email = email[0]['email']
			phone = empDetail.objects.filter(emp_id=emp_id).values('phone')
			Phone = phone[0]['phone']
			dept_id = empDetail.objects.filter(emp_id=emp_id).values('dept_id')

			emp_id = empDetail.objects.filter(emp_id=emp_id).values('emp_id')
			Emp_id = emp_id[0]['emp_id']

			context = {'username':Username,
			'password':password,
			'first_name':First_name,
			'email':Email,
			'phone':Phone,
			'dept_id':dept_id}
			phone_otp('12345',Phone)
			hashed_pwd = make_password(random_otp)
			User.objects.filter(emp_id=emp_id).update(password=hashed_pwd)


	return render(request,'login.html')

def otp(request):
	form_otp = forms.LoginForm()
	return render(request,'otp.html',{'form_otp':form_otp})



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

	form1 = forms.form_empDetail()
	form2 = forms.form_empDetailForm()
	form3 = forms.form_feedbackTab()
	form4 = forms.form_rd()

	# if request.method == 'POST':
	# 	if form1.is_valid() and form2.is_valid() and form3.is_valid() and form4.is_valid():



	return render(request,'assistant_form.html',{'form1':form1,'form2':form2,'form3':form3,'form4':form4})
