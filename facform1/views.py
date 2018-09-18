from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from . import forms
import urllib.parse as ap
import urllib.request
from django.contrib.auth.hashers import make_password, check_password
import random
from django.db.models import Q
from itertools import chain



# def phone_otp(random_otp, phone):
# 		phone1 = str(phone)
# 		message = 'Please login with the OTP: '+random_otp
# 		params = { 'number' : phone1, 'text' : message }
# 		baseUrl = 'https://www.smsgatewayhub.com/api/mt/SendSMS?APIKey=62sxGWT6MkCjDul6eNKejw&senderid=BMSITM&channel=2&DCS=0&flashsms=0&' + ap.urlencode(params)
# 		urllib.request.urlopen(baseUrl).read(1000)


def login(request):
	if(request.method=='POST'):

		userna = request.POST.get('username')
		username = userna.upper()

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
		if request.user.teach_status == True:
			return HttpResponseRedirect("/logout/")
		return HttpResponseRedirect("/assistant_form/")

	elif request.user.is_associate_professor():
		if request.user.teach_status == True:
			return HttpResponseRedirect("/logout/")
		return HttpResponseRedirect("/associate_form/")

	elif request.user.is_professor():
		if request.user.teach_status == True:
			return HttpResponseRedirect("/logout/")
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





def hod_first(request):
	return render(request,'hod_first.html')


def hod_display(request):

	user = request.user
	pk = request.user.pk
	hod_dept = user.department
	hod_desg = user.designation
	c1 = User.objects.filter(department=hod_dept).filter(designation__pk=11)
	c2 = User.objects.filter(department=hod_dept).filter(designation__pk=9)
	c3 = User.objects.filter(department=hod_dept).filter(designation__pk=10)

	c4 = list(chain(c2,c3))
	# c2 = .objects.filter(info__department=hod_dept).filter(~Q(info__designation=hod_desg))

	context = {'name':c1,'name1':c4 ,'hod_dept':hod_dept}

	# print(data6)
	return render(request,'hod_display.html',context=context)

def hod_teacher_display(request,pk):
	name =  User.objects.get(pk = pk);
	print(name)
	data1 = User.objects.get(username=name);
	print(data1.first_name)
	data2 = empDetailForm.objects.get(info__username=name);
	data3 = feedbackTab.objects.get(info__username=name);
	data4 = rd.objects.get(info__username=name);
	data5 = remarks.objects.get(info__username=name);





	if request.method == 'POST':
		form1 = forms.form_remarks1(request.POST)
		if form1.is_valid():

			sendme = User.objects.get(username=name)
			obj = form1.save(commit=False)

			obj.info = name
			obj.save()

			if sendme.hod_status == False:
				sendme.hod_status = True
				sendme.save()
			return HttpResponseRedirect("/logout/")

	else:
		form1 = forms.form_remarks1()


	context1 = {
	"key1":data1,
	"key2":data2,
	"key3":data3,
	"key4":data4,
	"key5":data5,
	"form1":form1
	}

	return render(request,'hod_teacher_display.html',context=context1)

def hod_teacher1_display(request,pk):
	name =  User.objects.get(pk = pk);
	print(name)
	data1 = User.objects.get(username=name);
	print(data1.first_name)
	data2 = empDetailForm.objects.get(info__username=name);
	data3 = feedbackTab.objects.get(info__username=name);
	data4 = rd.objects.get(info__username=name);
	data5 = remarks.objects.get(info__username=name);





	if request.method == 'POST':
		form1 = forms.form_remarks1(request.POST)
		if form1.is_valid():

			sendme = User.objects.get(username=name)
			obj = form1.save(commit=False)

			obj.info = name
			obj.save()

			if sendme.hod_status == False:
				sendme.hod_status = True
				sendme.save()
			return HttpResponseRedirect("/logout/")

	else:
		form1 = forms.form_remarks1()


	context1 = {
	"key1":data1,
	"key2":data2,
	"key3":data3,
	"key4":data4,
	"key5":data5,
	"form1":form1
	}

	return render(request,'hod_teacher1_display.html',context=context1)

def principal_first(request):
	dept = Department.objects.all()
	context = {'dept':dept}
	return render(request,'principal_first.html',context=context)

def principal_display(request,dept):

	print(dept)
	hod = User.objects.filter(department__name=dept).filter(designation__pk = 8)

	teach = User.objects.filter(department__name=dept).filter(designation__pk = 9)
	teach1 = User.objects.filter(department__name=dept).filter(designation__pk = 10)

	teach3 = list(chain(teach,teach1))
	teach2 = User.objects.filter(department__name=dept).filter(designation__pk = 11)

<<<<<<< Updated upstream

	dept = {'dept':dept,'hod':hod,'teach3':teach3,'teach2':teach2}



	print(hod)
	print(teach)

=======
	dept = {'dept':dept,'hod':hod,'teach':teach3,'teach2':teach2}

>>>>>>> Stashed changes

	return render(request,'principal_display.html',context=dept)


def principal_teacher_display(request,pk):
	name =  User.objects.get(pk = pk);
	print(name)
	data1 = User.objects.get(username=name);
	print(data1.department)

	data2 = empDetailForm.objects.get(info__username=name);
	data3 = feedbackTab.objects.get(info__username=name);
	data4 = rd.objects.get(info__username=name);
	data5 = remarks.objects.get(info__username=name);
	data6 = remarks1.objects.get(info__username=name);




	if request.method == 'POST':
		form1 = forms.form_remarks2(request.POST)

		if form1.is_valid():
			print("logout")
			sendme = User.objects.get(username=name)
			obj = form1.save(commit=False)

			obj.info = name
			obj.department = data1.department
			obj.save()

			if sendme.principal_status == False:
				sendme.principal_status = True
				sendme.save()

			return HttpResponseRedirect("/logout/")

	else:
		form1 = forms.form_remarks2()


	context1 = {
	"key1":data1,
	"key2":data2,
	"key3":data3,
	"key4":data4,
	"key5":data5,
	"key6":data6,
	"form1":form1
	}

	return render(request,'principal_teacher_display.html',context=context1)

def principal_teacher1_display(request,pk):
	name =  User.objects.get(pk = pk);
	print(name)
	data1 = User.objects.get(username=name);
	print(data1.department)

	data2 = empDetailForm.objects.get(info__username=name);
	data3 = feedbackTab.objects.get(info__username=name);
	data4 = rd.objects.get(info__username=name);
	data5 = remarks.objects.get(info__username=name);
	data6 = remarks1.objects.get(info__username=name);




	if request.method == 'POST':
		form1 = forms.form_remarks2(request.POST)

		if form1.is_valid():
			print("logout")
			sendme = User.objects.get(username=name)
			obj = form1.save(commit=False)

			obj.info = name
			obj.department = data1.department
			obj.save()

			if sendme.principal_status == False:
				sendme.principal_status = True
				sendme.save()

			return HttpResponseRedirect("/logout/")

	else:
		form1 = forms.form_remarks2()


	context1 = {
	"key1":data1,
	"key2":data2,
	"key3":data3,
	"key4":data4,
	"key5":data5,
	"key6":data6,
	"form1":form1
	}

	return render(request,'principal_teacher1_display.html',context=context1)

def principal_hod_display(request,pk):
	name =  User.objects.get(pk = pk);
	print(name)
	data1 = User.objects.get(username=name);
	print(data1.department)

	data2 = empDetailForm.objects.get(info__username=name);
	data3 = feedbackTab.objects.get(info__username=name);
	data4 = rd.objects.get(info__username=name);
	data5 = remarks.objects.get(info__username=name);




	if request.method == 'POST':
		form1 = forms.form_remarks2(request.POST)

		if form1.is_valid():
			print("logout")
			sendme = User.objects.get(username=name)
			obj = form1.save(commit=False)

			obj.info = name
			obj.department = data1.department
			obj.save()

			if sendme.principal_status == False:
				sendme.principal_status = True
				sendme.save()

			return HttpResponseRedirect("/logout/")

	else:
		form1 = forms.form_remarks2()


	context1 = {
	"key1":data1,
	"key2":data2,
	"key3":data3,
	"key4":data4,
	"key5":data5,
	"form1":form1
	}

	return render(request,'principal_hod_display.html',context=context1)

def ao_first(request):
	dept = Department.objects.all()
	context = {'dept':dept}
	return render(request,'ao_first.html',context=context)



def ao_display(request,dept):

	print(dept)
	a = "assistant"
	b = "associate"
	c = "professor"
	d = "hod"
	above = remarks2.objects.filter(total_marks__gte = 60).filter(department__name=dept).filter(info__designation__pk=11)
	above1 = remarks2.objects.filter(total_marks__gte = 60).filter(department__name=dept).filter(info__designation__pk=9)
	above2 = remarks2.objects.filter(total_marks__gte = 60).filter(department__name=dept).filter(info__designation__pk=10)
	above3 = remarks2.objects.filter(total_marks__gte = 60).filter(department__name=dept).filter(info__designation__pk=8)

	above4 = list(chain(above1,above2))

	below = remarks2.objects.filter(total_marks__lt = 60).filter(department__name=dept).filter(info__designation__pk=11)
	below1 = remarks2.objects.filter(total_marks__lt = 60).filter(department__name=dept).filter(info__designation__pk=9)
	below2 = remarks2.objects.filter(total_marks__lt = 60).filter(department__name=dept).filter(info__designation__pk=10)
	below3 = remarks2.objects.filter(total_marks__lt = 60).filter(department__name=dept).filter(info__designation__pk=8)

	below4 = list(chain(below1,below2))
	general = User.objects.filter(department__name=dept)
	tt = general.count()
	principal_completed = (User.objects.filter(department__name=dept).filter(principal_status=True)).count()
	hod_completed  = (User.objects.filter(department__name=dept).filter(hod_status=True)).count()
	teach_completed  = (User.objects.filter(department__name=dept).filter(teach_status=True)).count()


	dept = {'dept':dept,'above':above,'above1':above4,'above3':above3,'below':below,'below1':below4,'below3':below3,'general':general,'p':principal_completed,'h':hod_completed,'t':teach_completed,'total':tt}
<<<<<<< Updated upstream

>>>>>>> Stashed changes
=======
	
>>>>>>> Stashed changes


	return render(request,'ao_display.html',context=dept)

def ao_approved(request,dept):

	general = remarks2.objects.filter(department__name=dept)
	dept = {'dept':dept,'general':general}
	return render(request,'ao_approved.html',context=dept)


def ao_teacher_display(request,name):
	print(name)
	data1 = User.objects.get(username=name);
	data2 = empDetailForm.objects.get(info__username=name);
	data3 = feedbackTab.objects.get(info__username=name);
	data4 = rd.objects.get(info__username=name);
	data5 = remarks.objects.get(info__username=name);
	data6 = remarks1.objects.get(info__username=name);
	data7 = remarks2.objects.get(info__username=name);



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


def ao_teacher1_display(request,name):
	print(name)
	data1 = User.objects.get(username=name);
	data2 = empDetailForm.objects.get(info__username=name);
	data3 = feedbackTab.objects.get(info__username=name);
	data4 = rd.objects.get(info__username=name);
	data5 = remarks.objects.get(info__username=name);
	data6 = remarks1.objects.get(info__username=name);
	data7 = remarks2.objects.get(info__username=name);



	context1 = {
	"key1":data1,
	"key2":data2,
	"key3":data3,
	"key4":data4,
	"key5":data5,
	"key6":data6,
	"key7":data7,


	}
	return render(request,'ao_teacher1_display.html',context=context1)

def ao_hod_display(request,name):
	print(name)
	data1 = User.objects.get(username=name);
	data2 = empDetailForm.objects.get(info__username=name);
	data3 = feedbackTab.objects.get(info__username=name);
	data4 = rd.objects.get(info__username=name);
	data5 = remarks.objects.get(info__username=name);
	data7 = remarks2.objects.get(info__username=name);



	context1 = {
	"key1":data1,
	"key2":data2,
	"key3":data3,
	"key4":data4,
	"key5":data5,
	"key7":data7,


	}
	return render(request,'ao_hod_display.html',context=context1)


def hod_first(request):
	user = request.user
	hod_dept = user.department
	context = {'dept':hod_dept}
	return render(request,'hod_first.html',context=context)




def logout(request):
	return render(request,'hod_success.html')



def f_assistant(request):
	user = request.user
	print(user)
	data_final = User.objects.get(username=user)



	if request.method == 'POST':
		form1 = forms.form_User(request.POST)
		form2 = forms.form_empDetailForm(request.POST)
		form3 = forms.form_feedbackTab(request.POST)
		form4 = forms.form_rd(request.POST)
		form5 = forms.form_remarks(request.POST)
		if form1.is_valid() and form2.is_valid() and form3.is_valid() and form4.is_valid() and form5.is_valid():

			sendme = User.objects.get(username=request.user)

			obj0 = form1.save(commit=False)
			obj = form2.save(commit=False)
			obj1 = form3.save(commit=False)
			obj2 = form4.save(commit=False)
			obj3 = form5.save(commit=False)


			obj0.info = request.user
			obj.info = request.user
			obj1.info = request.user
			obj2.info = request.user
			obj3.info = request.user

			obj0.save()
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
		form1 = forms.form_User()
		form2 = forms.form_empDetailForm()
		form3 = forms.form_feedbackTab()
		form4 = forms.form_rd()
		form5 = forms.form_remarks()
	return render(request,'assistant_form.html',{'form1':form1,'form2':form2,'form3':form3,'form4':form4,'form5':form5,'info':data_final})

def f_associate(request):
	user = request.user
	print(user)
	data_final = User.objects.get(username=user)



	if request.method == 'POST':
		form1 = forms.form_User(request.POST)
		form2 = forms.form_empDetailForm(request.POST)
		form3 = forms.form_feedbackTab(request.POST)
		form4 = forms.form_rd(request.POST)
		form5 = forms.form_remarks(request.POST)
		if form1.is_valid() and form2.is_valid() and form3.is_valid() and form4.is_valid() and form5.is_valid():

			sendme = User.objects.get(username=request.user)

			obj0 = form1.save(commit=False)
			obj = form2.save(commit=False)
			obj1 = form3.save(commit=False)
			obj2 = form4.save(commit=False)
			obj3 = form5.save(commit=False)


			obj0.info = request.user
			obj.info = request.user
			obj1.info = request.user
			obj2.info = request.user
			obj3.info = request.user

			obj0.save()
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
		form1 = forms.form_User()
		form2 = forms.form_empDetailForm()
		form3 = forms.form_feedbackTab()
		form4 = forms.form_rd()
		form5 = forms.form_remarks()
	return render(request,'associate_form.html',{'form1':form1,'form2':form2,'form3':form3,'form4':form4,'form5':form5,'info':data_final})


def hod_form(request):
	user = request.user
	if request.user.teach_status == False:
		data_final = User.objects.get(username=user)



		if request.method == 'POST':
			form1 = forms.form_User(request.POST)
			form2 = forms.form_empDetailForm(request.POST)
			form3 = forms.form_feedbackTab(request.POST)
			form4 = forms.form_rd(request.POST)
			form5 = forms.form_remarks(request.POST)
			if form1.is_valid() and form2.is_valid() and form3.is_valid() and form4.is_valid() and form5.is_valid():

				sendme = User.objects.get(username=request.user)

				obj0 = form1.save(commit=False)
				obj = form2.save(commit=False)
				obj1 = form3.save(commit=False)
				obj2 = form4.save(commit=False)
				obj3 = form5.save(commit=False)


				obj0.info = request.user
				obj.info = request.user
				obj1.info = request.user
				obj2.info = request.user
				obj3.info = request.user

				obj0.save()
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
			form1 = forms.form_User()
			form2 = forms.form_empDetailForm()
			form3 = forms.form_feedbackTab()
			form4 = forms.form_rd()
			form5 = forms.form_remarks()
		return render(request,'hod_form.html',{'form1':form1,'form2':form2,'form3':form3,'form4':form4,'form5':form5,'info':data_final})

	else:
		return HttpResponseRedirect("/hod_first/")
