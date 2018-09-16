from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from . import forms
import urllib.parse as ap
import urllib.request
from django.contrib.auth.hashers import make_password, check_password
import random
from django.db.models import Q
import itertools



# def phone_otp(random_otp, phone):
# 		phone1 = str(phone)
# 		message = 'Please login with the OTP: '+random_otp
# 		params = { 'number' : phone1, 'text' : message }
# 		baseUrl = 'https://www.smsgatewayhub.com/api/mt/SendSMS?APIKey=62sxGWT6MkCjDul6eNKejw&senderid=BMSITM&channel=2&DCS=0&flashsms=0&' + ap.urlencode(params)
# 		urllib.request.urlopen(baseUrl).read(1000)


def login(request):
	if(request.method=='POST'):

		username = request.POST.get('username')

		if(User.objects.filter(username=username).exists()):
			user = User.objects.get(username=username)
			first_name = user.first_name
			email = user.email
			phone = user.phone
			# random_otp = r''.join(random.choice('01234ABCD') for i in range(8))
			random_otp = "123456"
			print(random_otp)
			#phone_otp(random_otp,phone)

			hashed_pwd = make_password(random_otp)
			User.objects.filter(username=username).update(password=hashed_pwd)

			return HttpResponseRedirect("/login/user=" + username)

	return render(request,'login.html')

def decide_view(request):
	if request.user.is_assistant_professor():
		# print('assis')
		return HttpResponseRedirect("/assistant_form/")

	elif request.user.is_associate_professor():
		print('asso')
		return HttpResponseRedirect("/associate_form/")

	elif request.user.is_hod():
		# print('hod')
		return HttpResponseRedirect("/hod_first/")

	elif request.user.is_principal():
		print('princy')
		return HttpResponseRedirect("/principal_first/")

	elif request.user.is_ao():
		return HttpResponseRedirect("/ao_first/")

	# else:
	# 	return HttpResponseRedirect("/")
# def front(request):
# 	return render(request,'front.html')




def hod_form(request):
	if request.method == 'POST':
		form2 = forms.form_empDetailForm(request.POST)
		form3 = forms.form_feedbackTab(request.POST)
		form4 = forms.form_rd(request.POST)
		form5 = forms.form_remarks(request.POST)
		if  form2.is_valid() and form3.is_valid() and form4.is_valid() and form5.is_valid():
			obj = form2.save(commit=False)
			obj1 = form3.save(commit=False)
			obj2 = form4.save(commit=False)
			obj3 = form5.save(commit=False)

			obj.info = request.user
			obj1.info = request.user
			obj2.info = request.user
			obj3.info = request.user
			obj.save()
			obj1.save()
			obj2.save()
			obj3.teach_status = True
			obj3.save()


			return HttpResponseRedirect("/logout/")
		else:
			print(form2.errors)
	else:

		form2 = forms.form_empDetailForm()
		form3 = forms.form_feedbackTab()
		form4 = forms.form_rd()
		form5 = forms.form_remarks()

	return render(request,'hod_form.html',{'form2':form2,'form3':form3,'form4':form4,'form5':form5})

def hod_first(request):
	return render(request,'hod_first.html')


def hod_display(request):

	user = request.user
	pk = request.user.pk
	hod_dept = user.department
	hod_desg = user.designation
	c1 = User.objects.filter(department=hod_dept).filter(~Q(designation=hod_desg))
	# c2 = .objects.filter(info__department=hod_dept).filter(~Q(info__designation=hod_desg))



	context = {'name':c1,'hod_dept':hod_dept}

	# print(data6)
	return render(request,'hod_display.html',context=context)

def hod_teacher_display(request,pk):
	name =  User.objects.get(pk = pk);
	print(name)
	data1 = User.objects.get(username=name);
	data2 = empDetailForm.objects.get(info__username=name);
	data3 = feedbackTab.objects.get(info__username=name);
	data4 = rd.objects.get(info__username=name);
	data5 = remarks.objects.get(info__username=name);
	print(data2.Present_pos)


	context1 = {
	"key1":data1,
	"key2":data2,
	"key3":data3,
	"key4":data4,
	"key5":data5,
	}
	return render(request,'hod_teacher_display.html',context=context1)


def principal_first(request):
	dept = Department.objects.all()
	context = {'dept':dept}
	return render(request,'principal_first.html',context=context)

def principal_display(request,dept):

	print(dept)
	hod = User.objects.filter(department__name=dept).filter(designation__pk = 8)
	teach = User.objects.filter(department__name=dept).filter(~Q(designation__pk = 8))
	dept = {'dept':dept,'hod':hod,'teach':teach}
	print(hod)
	print(teach)

	return render(request,'principal_display.html',context=dept)



def ao_first(request):
	dept = Department.objects.all()
	context = {'dept':dept}
	return render(request,'ao_first.html',context=context)



def ao_display(request,dept):

	print(dept)
	above = remarks2.objects.filter(total_marks__gte = 60).filter(department__name=dept)
	below = remarks2.objects.filter(total_marks__lt = 60).filter(department__name=dept)
	
	dept = {'dept':dept,'above':above,'below':below}
	print(above)
	print(below)

	return render(request,'ao_display.html',context=dept)


def ao_teacher_display(request,pk):
	name =  User.objects.get(pk = pk);
	print(name)
	data1 = User.objects.get(username=name);
	data2 = empDetailForm.objects.get(info__username=name);
	data3 = feedbackTab.objects.get(info__username=name);
	data4 = rd.objects.get(info__username=name);
	data5 = remarks.objects.get(info__username=name);
	data6 = remarks1.objects.get(info__username=name);
	data7 = remarks2.objects.get(info__username=name);

	print(data2.Present_pos)


	context1 = {
	"key1":data1,
	"key2":data2,
	"key3":data3,
	"key4":data4,
	"key5":data5,
	"key6":data6,
	"key7":data7,


	}
	return render(request,'ao_teacher_display.html',context=context1)



def logout(request):
	return render(request,'hod_success.html')



def f_assistant(request):
	if request.method == 'POST':
		form2 = forms.form_empDetailForm(request.POST)
		form3 = forms.form_feedbackTab(request.POST)
		form4 = forms.form_rd(request.POST)
		form5 = forms.form_remarks(request.POST)
		if form2.is_valid() and form3.is_valid() and form4.is_valid() and form5.is_valid():

			sendme = User.objects.get(username=request.user)

			obj = form2.save(commit=False)
			obj1 = form3.save(commit=False)
			obj2 = form4.save(commit=False)
			obj3 = form5.save(commit=False)


			obj.info = request.user
			obj1.info = request.user
			obj2.info = request.user
			obj3.info = request.user

			obj.save()
			obj1.save()
			obj2.save()
			obj3.save()

			if sendme.teach_status == False:
				sendme.teach_status = True
				sendme.save()

			return HttpResponseRedirect("/logout/")
		else:
			print(form2.errors)
	else:

		form2 = forms.form_empDetailForm()
		form3 = forms.form_feedbackTab()
		form4 = forms.form_rd()
		form5 = forms.form_remarks()
	return render(request,'assistant_form.html',{'form2':form2,'form3':form3,'form4':form4,'form5':form5})

def f_associate(request):
	if request.method == 'POST':
		form2 = forms.form_empDetailForm(request.POST)
		form3 = forms.form_feedbackTab(request.POST)
		form4 = forms.form_rd(request.POST)
		form5 = forms.form_remarks(request.POST)
		if  form2.is_valid() and form3.is_valid() and form4.is_valid() and form5.is_valid():
			obj = form2.save(commit=False)
			obj1 = form3.save(commit=False)
			obj2 = form4.save(commit=False)
			obj3 = form5.save(commit=False)

			obj.info = request.user
			obj1.info = request.user
			obj2.info = request.user
			obj3.info = request.user
			obj.save()
			obj1.save()
			obj2.save()
			obj3.teach_status = True
			obj3.save()


			return HttpResponseRedirect("/logout/")
		else:
			print(form2.errors)
	else:

		form2 = forms.form_empDetailForm()
		form3 = forms.form_feedbackTab()
		form4 = forms.form_rd()
		form5 = forms.form_remarks()

	return render(request,'associate_form.html',{'form2':form2,'form3':form3,'form4':form4,'form5':form5})
