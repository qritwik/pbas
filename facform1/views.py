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

from django.contrib.auth.decorators import login_required
from django.forms import formset_factory


def ao_consolidated(request):
	data1 = User.objects.all().order_by('department')
	data2 = feedbackTab.objects.all()
	data3 = rd.objects.all()
	data4 = remarks1.objects.all()
	data5 = remarks2.objects.all()

	print(data1.count())
	print(data2.count())
	print(data3.count())
	print(data4.count())



	data6 = zip(data1,data2,data3,data4,data5)







	context = {
			'data1':data1,
			'data2':data2,
			'data3':data3,
			'data4':data4,
			'data5':data5,
			'data6':data6


		}
	return render(request,'ao_consolidated.html',context = context)




def phone_otp(random_otp, phone):
		phone1 = str(phone)
		message = 'Please login with the OTP: '+random_otp
		params = { 'number' : phone1, 'text' : message }
		baseUrl = 'https://www.smsgatewayhub.com/api/mt/SendSMS?APIKey=62sxGWT6MkCjDul6eNKejw&senderid=BMSITM&channel=2&DCS=0&flashsms=0&' + ap.urlencode(params)
		urllib.request.urlopen(baseUrl).read(1000)


def invalid(request):
	return render(request,'invalid.html')

def login(request):
	if(request.method=='POST'):

		userna = request.POST.get('username')
		username = userna.upper()

		if(User.objects.filter(username=username).exists()):
			user = User.objects.get(username=username)
			first_name = user.first_name
			email = user.email
			phone = user.phone
			random_otp = r''.join(random.choice('0123456789') for i in range(4))
			phone_otp(random_otp,phone)

			hashed_pwd = make_password(random_otp)
			User.objects.filter(username=username).update(password=hashed_pwd)

			return HttpResponseRedirect("/login/user=" + username)

	return render(request,'login.html')

def decide_view(request):
	if request.user.is_assistant_professor():
		if request.user.teach_status == True:
			return HttpResponseRedirect("/assistant_preview/")
		return HttpResponseRedirect("/assistant_form1/")

	elif request.user.is_associate_professor():
		if request.user.teach_status == True:
			return HttpResponseRedirect("/associate_preview/")
		return HttpResponseRedirect("/associate_form1/")

	elif request.user.is_professor():
		if request.user.teach_status == True:
			return HttpResponseRedirect("/associate_preview/")
		return HttpResponseRedirect("/associate_form1/")

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






@login_required
def hod_display(request):

	user = request.user
	hod_dept = user.department
	if request.user.is_hod() and request.user.department == hod_dept:

		user = request.user
		pk = request.user.pk

		hod_desg = user.designation
		c1 = User.objects.filter(department=hod_dept).filter(designation__pk=11)
		c2 = User.objects.filter(department=hod_dept).filter(designation__pk=9)
		c3 = User.objects.filter(department=hod_dept).filter(designation__pk=10)

		c4 = list(chain(c2,c3))
		# c2 = .objects.filter(info__department=hod_dept).filter(~Q(info__designation=hod_desg))

		context = {'name':c1,'name1':c4 ,'hod_dept':hod_dept}

		# print(data6)
		return render(request,'hod_display.html',context=context)
	else:
		return HttpResponseRedirect('/invalid')

@login_required
def hod_teacher_display(request,pk):
		if request.user.is_hod():
			name =  User.objects.get(pk = pk);
			print(name)
			data1 = User.objects.get(username=name);
			print(data1.first_name)
			data2 = empDetailForm.objects.get(info__username=name);
			data3 = feedbackTab.objects.get(info__username=name);
			data4 = rd.objects.get(info__username=name);
			data5 = remarks.objects.get(info__username=name);
			data6 = conference.objects.get(info__username=name);
			data7 = journal.objects.get(info__username=name);






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
					return HttpResponseRedirect("/hod_first/")

			else:
				form1 = forms.form_remarks1()


			context1 = {
			"key1":data1,
			"key2":data2,
			"key3":data3,
			"key4":data4,
			"key5":data5,
			"key6":data6,
			"key7":data7,
			"form1":form1
			}

			return render(request,'hod_teacher_display.html',context=context1)
		else:
			return HttpResponseRedirect('/invalid')


@login_required
def hod_teacher1_display(request,pk):
	if request.user.is_hod():
		name =  User.objects.get(pk = pk);
		print(name)
		data1 = User.objects.get(username=name);
		print(data1.first_name)
		data2 = empDetailForm.objects.get(info__username=name);
		data3 = feedbackTab.objects.get(info__username=name);
		data4 = rd.objects.get(info__username=name);
		data5 = remarks.objects.get(info__username=name);
		data6 = conference.objects.get(info__username=name);
		data7 = journal.objects.get(info__username=name);





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
				return HttpResponseRedirect("/hod_first/")

		else:
			form1 = forms.form_remarks1()


		context1 = {
		"key1":data1,
		"key2":data2,
		"key3":data3,
		"key4":data4,
		"key5":data5,
		"key6":data6,
		"key7":data7,
		"form1":form1
		}

		return render(request,'hod_teacher1_display.html',context=context1)

	else:
		return HttpResponseRedirect('/invalid')

@login_required
def principal_first(request):
	if request.user.is_principal():
		dept = Department.objects.all()






		context = {'dept':dept}


		return render(request,'principal_first.html',context=context)
	else:
		return HttpResponseRedirect('/invalid')


@login_required
def principal_display(request,dept):
	if request.user.is_principal():

		print(dept)
		hod = User.objects.filter(department__name=dept).filter(designation__pk = 8).filter(teach_status=True)

		teach = User.objects.filter(department__name=dept).filter(designation__pk = 9).filter(hod_status=True)
		teach1 = User.objects.filter(department__name=dept).filter(designation__pk = 10).filter(hod_status=True)

		teach3 = list(chain(teach,teach1))
		teach2 = User.objects.filter(department__name=dept).filter(designation__pk = 11).filter(hod_status=True)


		dept = {'dept':dept,'hod':hod,'teach3':teach3,'teach2':teach2}



		return render(request,'principal_display.html',context=dept)
	else:
		return HttpResponseRedirect('/invalid')


@login_required
def principal_teacher_display(request,pk):
	if request.user.is_principal():
		name =  User.objects.get(pk = pk);
		print(name)
		data1 = User.objects.get(username=name);
		print(data1.department)

		data2 = empDetailForm.objects.get(info__username=name);
		data3 = feedbackTab.objects.get(info__username=name);
		data4 = rd.objects.get(info__username=name);
		data5 = remarks.objects.get(info__username=name);
		data6 = conference.objects.get(info__username=name);
		data7 = journal.objects.get(info__username=name);
		data8 = remarks1.objects.get(info__username=name);




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

				return HttpResponseRedirect("/principal_display/"+ data1.department.name)

		else:
			form1 = forms.form_remarks2()


		context1 = {
		"key1":data1,
		"key2":data2,
		"key3":data3,
		"key4":data4,
		"key5":data5,
		"key6":data6,
		"key7":data7,
		"key8":data8,
		"form1":form1
		}

		return render(request,'principal_teacher_display.html',context=context1)
	else:
		return HttpResponseRedirect('/invalid')


@login_required
def principal_teacher1_display(request,pk):
	if request.user.is_principal():
		name =  User.objects.get(pk = pk);
		print(name)
		data1 = User.objects.get(username=name);
		print(data1.department)

		data2 = empDetailForm.objects.get(info__username=name);
		data3 = feedbackTab.objects.get(info__username=name);
		data4 = rd.objects.get(info__username=name);
		data5 = remarks.objects.get(info__username=name);
		data6 = conference.objects.get(info__username=name);
		data7 = journal.objects.get(info__username=name);
		if User.objects.filter(username=name).filter(hod_status=True):
			data8 = remarks1.objects.get(info__username=name)
		else:
			data8 = []



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

				return HttpResponseRedirect("/principal_display/"+data1.department.name)

		else:
			form1 = forms.form_remarks2()


		context1 = {
		"key1":data1,
		"key2":data2,
		"key3":data3,
		"key4":data4,
		"key5":data5,
		"key6":data6,
		"key7":data7,
		"key8":data8,
		"form1":form1
		}

		return render(request,'principal_teacher1_display.html',context=context1)
	else:
		return HttpResponseRedirect('/invalid')


@login_required
def principal_hod_display(request,pk):
	if request.user.is_principal():
		name =  User.objects.get(pk = pk);
		print(name)
		data1 = User.objects.get(username=name);
		print(data1.department)

		data2 = empDetailForm.objects.get(info__username=name);
		data3 = feedbackTab.objects.get(info__username=name);
		data4 = rd.objects.get(info__username=name);
		data5 = remarks.objects.get(info__username=name);
		data6 = conference.objects.get(info__username=name);
		data7 = journal.objects.get(info__username=name);




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

				return HttpResponseRedirect("/principal_display/"+data1.department.name)

		else:
			form1 = forms.form_remarks2()


		context1 = {
		"key1":data1,
		"key2":data2,
		"key3":data3,
		"key4":data4,
		"key5":data5,
		"key6":data6,
		"key7":data7,
		"form1":form1
		}

		return render(request,'principal_hod_display.html',context=context1)
	else:
		return HttpResponseRedirect('/invalid')

@login_required
def ao_first(request):
	if request.user.is_ao():
		dept = Department.objects.all()
		context = {'dept':dept}
		return render(request,'ao_first.html',context=context)
	else:
		return HttpResponseRedirect('/invalid')



@login_required
def ao_display(request,dept):
	if request.user.is_ao():

		print(dept)
		a = "assistant"
		b = "associate"
		c = "professor"
		d = "hod"
		# above = remarks2.objects.filter(total_marks__gte = 60).filter(department__name=dept).filter(info__designation__pk=11)
		# above1 = remarks2.objects.filter(total_marks__gte = 60).filter(department__name=dept).filter(info__designation__pk=9)
		# above2 = remarks2.objects.filter(total_marks__gte = 60).filter(department__name=dept).filter(info__designation__pk=10)
		# above3 = remarks2.objects.filter(total_marks__gte = 60).filter(department__name=dept).filter(info__designation__pk=8)
		#
		# above4 = list(chain(above1,above2))
		#
		# below = remarks2.objects.filter(total_marks__lt = 60).filter(department__name=dept).filter(info__designation__pk=11)
		# below1 = remarks2.objects.filter(total_marks__lt = 60).filter(department__name=dept).filter(info__designation__pk=9)
		# below2 = remarks2.objects.filter(total_marks__lt = 60).filter(department__name=dept).filter(info__designation__pk=10)
		# below3 = remarks2.objects.filter(total_marks__lt = 60).filter(department__name=dept).filter(info__designation__pk=8)
		#
		# below4 = list(chain(below1,below2))
		general = User.objects.filter(department__name=dept)
		tt = general.count()
		principal_completed = (User.objects.filter(department__name=dept).filter(principal_status=True)).count()
		hod_completed  = (User.objects.filter(department__name=dept).filter(hod_status=True)).count()
		teach_completed  = (User.objects.filter(department__name=dept).filter(teach_status=True)).count()


		context = {'dept':dept,'general':general,'p':principal_completed,'h':hod_completed,'t':teach_completed,'total':tt}

		return render(request,'ao_display.html',context=context)
	else:
		return HttpResponseRedirect('/invalid')

@login_required
def ao_approved(request,dept):
	if request.user.is_ao():


		general = remarks2.objects.filter(department__name=dept)
		dept = {'dept':dept,'general':general}
		return render(request,'ao_approved.html',context=dept)
	else:
		return HttpResponseRedirect('/invalid')



@login_required
def ao_teacher_display(request,name):
	print(name)
	data1 = User.objects.get(username=name)
	data2 = empDetailForm.objects.get(info__username=name)
	data3 = feedbackTab.objects.get(info__username=name)
	data4 = rd.objects.get(info__username=name)
	data5 = remarks.objects.get(info__username=name)
	data6 = conference.objects.get(info__username=name)
	data7 = journal.objects.get(info__username=name)

	if User.objects.filter(username=name).filter(hod_status=True):
		data8 = remarks1.objects.get(info__username=name)
	else:
		data8 = []
	if User.objects.filter(username=name).filter(principal_status=True):
		data9 = remarks2.objects.get(info__username=name)
	else:
		data9 = []
	# if remarks1.objects.get(info__username=name):
	# 	data8 = remarks1.objects.get(info__username=name)
	#
	# if remarks2.objects.get(info__username=name):
	# 	data9 = remarks2.objects.get(info__username=name)







	context1 = {
	"key1":data1,
	"key2":data2,
	"key3":data3,
	"key4":data4,
	"key5":data5,
	"key6":data6,
	"key7":data7,
	"key8":data8,
	"key9":data9,


	}
	return render(request,'ao_teacher_display.html',context=context1)

@login_required
def ao_teacher1_display(request,name):
	print(name)
	data1 = User.objects.get(username=name)
	data2 = empDetailForm.objects.get(info__username=name)
	data3 = feedbackTab.objects.get(info__username=name)
	data4 = rd.objects.get(info__username=name)
	data5 = remarks.objects.get(info__username=name)
	data6 = conference.objects.get(info__username=name);
	data7 = journal.objects.get(info__username=name);
	if User.objects.filter(username=name).filter(hod_status=True):
		data8 = remarks1.objects.get(info__username=name)
	else:
		data8 = []
	if User.objects.filter(username=name).filter(principal_status=True):
		data9 = remarks2.objects.get(info__username=name)
	else:
		data9 = []



	context1 = {
	"key1":data1,
	"key2":data2,
	"key3":data3,
	"key4":data4,
	"key5":data5,
	"key6":data6,
	"key7":data7,
	"key8":data8,
	"key9":data9,


	}
	return render(request,'ao_teacher1_display.html',context=context1)

@login_required
def ao_hod_display(request,name):
	if request.user.is_ao():
		print(name)
		data1 = User.objects.get(username=name)
		data2 = empDetailForm.objects.get(info__username=name)
		data3 = feedbackTab.objects.get(info__username=name)
		data4 = rd.objects.get(info__username=name)
		data5 = remarks.objects.get(info__username=name)
		data6 = conference.objects.get(info__username=name);
		data7 = journal.objects.get(info__username=name);
		if User.objects.filter(username=name).filter(principal_status=True):
			data8 = remarks2.objects.get(info__username=name)
		else:
			data8 = []



		context1 = {
		"key1":data1,
		"key2":data2,
		"key3":data3,
		"key4":data4,
		"key5":data5,
		"key6":data5,
		"key7":data7,
		"key8":data8,


		}
		return render(request,'ao_hod_display.html',context=context1)
	else:
		return HttpResponseRedirect('/invalid')

@login_required
def hod_first(request):
	if request.user.is_hod():

		user = request.user
		hod_dept = user.department
		context = {'dept':hod_dept,'user':user}
		return render(request,'hod_first.html',context=context)

	else:
		print("HI")
		return HttpResponseRedirect('/invalid')




def logout(request):
	return render(request,'hod_success.html')

@login_required
def f_assistant5(request):
	if request.user.is_assistant_professor():

		form6 = forms.form_conference()
		form7 = forms.form_journal()

		if conference.objects.filter(info=request.user).exists():

			return HttpResponseRedirect("/logout/")
		else:
			if request.method == 'POST':
				sendme = User.objects.get(username=request.user)
				form6 = forms.form_conference(request.POST)
				form7 = forms.form_journal(request.POST)
				if form6.is_valid() and form7.is_valid():
					obj3 = form6.save(commit=False)
					obj4 = form7.save(commit=False)
					obj3.info = request.user
					obj4.info = request.user

					obj3.save()
					obj4.save()

					if sendme.teach_status == False:
						sendme.teach_status = True
						sendme.save()
					return HttpResponseRedirect("/logout/")
			return render(request,'assistant_form5.html',{'form6':form6,'form7':form7})
		return render(request,'assistant_form5.html',{'form6':form6,'form7':form7})
	else:
		return HttpResponseRedirect('/invalid')

@login_required
def f_assistant4(request):
	if request.user.is_assistant_professor():
		form5 = forms.form_remarks()
		if remarks.objects.filter(info=request.user).exists():

			return HttpResponseRedirect("/assistant_form5/")
		else:
			if request.method == 'POST':

				form5 = forms.form_remarks(request.POST)
				if form5.is_valid():
					obj3 = form5.save(commit=False)
					obj3.info = request.user
					obj3.save()
					return HttpResponseRedirect("/assistant_form5/")
			return render(request,'assistant_form4.html',{'form5':form5})
		return render(request,'assistant_form4.html',{'form5':form5})
	else:
		return HttpResponseRedirect('/invalid')

@login_required
def f_assistant3(request):
	if request.user.is_assistant_professor():
		form4 = forms.form_rd()
		if rd.objects.filter(info=request.user).exists():

			return HttpResponseRedirect("/assistant_form4/")
		else:
			if request.method == 'POST':
				form4 = forms.form_rd(request.POST)
				if form4.is_valid():
					obj2 = form4.save(commit=False)
					obj2.info = request.user
					obj2.save()
					return HttpResponseRedirect("/assistant_form4/")
			return render(request,'assistant_form3.html',{'form4':form4})
		return render(request,'assistant_form3.html',{'form4':form4})
	else:
		return HttpResponseRedirect('/invalid')

@login_required
def f_assistant2(request):
	if request.user.is_assistant_professor():
		form3 = forms.form_feedbackTab()

		if feedbackTab.objects.filter(info=request.user).exists():

			return HttpResponseRedirect("/assistant_form3/")
		else:
			if request.method == 'POST':
				form3 = forms.form_feedbackTab(request.POST)
				if form3.is_valid():
					obj1 = form3.save(commit=False)
					obj1.info = request.user
					obj1.save()
					return HttpResponseRedirect("/assistant_form3/")
			return render(request,'assistant_form2.html',{'form3':form3})


		return render(request,'assistant_form2.html',{'form3':form3})
	else:
		return HttpResponseRedirect('/invalid')

@login_required
def f_assistant1(request):
	if request.user.is_assistant_professor():

		user = request.user
		print(user)
		data_final = User.objects.get(username=user)
		form1 = forms.form_User()
		form2 = forms.form_empDetailForm()

		if empDetailForm.objects.filter(info=user).exists():

			return HttpResponseRedirect("/assistant_form2/")

		else:

			if request.method == 'POST':
				form1 = forms.form_User(request.POST)
				form2 = forms.form_empDetailForm(request.POST)


				if form1.is_valid() and form2.is_valid():

					sendme = User.objects.get(username=request.user)

					obj = form2.save(commit=False)
					obj.info = request.user
					obj.save()

					sendme.doc_link  = 	form1.cleaned_data['doc_link']
					sendme.save()

					return HttpResponseRedirect("/assistant_form2/")
			return render(request,'assistant_form1.html',{'form1':form1,'form2':form2,'info':data_final})
		return render(request,'assistant_form1.html',{'form1':form1,'form2':form2,'info':data_final})
	else:
		return HttpResponseRedirect('/invalid')

@login_required
def f_associate5(request):
	if request.user.is_associate_professor() or request.user.is_professor() or request.user.username == 'HOD_CIVIL':

		form6 = forms.form_conference()
		form7 = forms.form_journal()

		if conference.objects.filter(info=request.user).exists():

			return HttpResponseRedirect("/logout/")
		else:
			if request.method == 'POST':
				sendme = User.objects.get(username=request.user)
				form6 = forms.form_conference(request.POST)
				form7 = forms.form_journal(request.POST)
				if form6.is_valid() and form7.is_valid():
					obj3 = form6.save(commit=False)
					obj4 = form7.save(commit=False)
					obj3.info = request.user
					obj4.info = request.user

					obj3.save()
					obj4.save()

					if sendme.teach_status == False:
						sendme.teach_status = True
						sendme.save()
					return HttpResponseRedirect("/logout/")
			else:
				print(form6.errors)
				print(form7.errors)
			return render(request,'associate_form5.html',{'form6':form6,'form7':form7})
		return render(request,'associate_form5.html',{'form6':form6,'form7':form7})
	else:
		return HttpResponseRedirect('/invalid')

@login_required
def f_associate4(request):
	if request.user.is_associate_professor() or request.user.is_professor() or request.user.username == 'HOD_CIVIL':
		form5 = forms.form_remarks()
		if remarks.objects.filter(info=request.user).exists():

			return HttpResponseRedirect("/associate_form5/")
		else:
			if request.method == 'POST':
				sendme = User.objects.get(username=request.user)
				form5 = forms.form_remarks(request.POST)
				if form5.is_valid():
					obj3 = form5.save(commit=False)
					obj3.info = request.user
					obj3.save()
					return HttpResponseRedirect("/associate_form5/")
			return render(request,'associate_form4.html',{'form5':form5})
		return render(request,'associate_form4.html',{'form5':form5})
	else:
		return HttpResponseRedirect('/invalid')

@login_required
def f_associate3(request):
	if request.user.is_associate_professor() or request.user.is_professor() or request.user.username == 'HOD_CIVIL':
		form4 = forms.form_rd()
		if rd.objects.filter(info=request.user).exists():

			return HttpResponseRedirect("/associate_form4/")
		else:
			if request.method == 'POST':
				form4 = forms.form_rd(request.POST)
				if form4.is_valid():
					obj2 = form4.save(commit=False)
					obj2.info = request.user
					obj2.save()
					return HttpResponseRedirect("/associate_form4/")
			return render(request,'associate_form3.html',{'form4':form4})
		return render(request,'associate_form3.html',{'form4':form4})
	else:
		return HttpResponseRedirect('/invalid')


@login_required
def f_associate2(request):
	if request.user.is_associate_professor() or request.user.is_professor() or request.user.username == 'HOD_CIVIL':
		form3 = forms.form_feedbackTab()

		if feedbackTab.objects.filter(info=request.user).exists():

			return HttpResponseRedirect("/associate_form3/")
		else:
			if request.method == 'POST':
				form3 = forms.form_feedbackTab(request.POST)
				if form3.is_valid():
					obj1 = form3.save(commit=False)
					obj1.info = request.user
					obj1.save()
					return HttpResponseRedirect("/associate_form3/")
			return render(request,'associate_form2.html',{'form3':form3})

		return render(request,'associate_form2.html',{'form3':form3})
	else:
		return HttpResponseRedirect('/invalid')


@login_required
def f_associate1(request):
	if request.user.is_associate_professor() or request.user.is_professor() or request.user.username == 'HOD_CIVIL':

		user = request.user
		print(user)
		data_final = User.objects.get(username=user)
		form1 = forms.form_User()
		form2 = forms.form_empDetailForm()

		if empDetailForm.objects.filter(info=user).exists():

			return HttpResponseRedirect("/associate_form2/")

		else:

			if request.method == 'POST':
				form1 = forms.form_User(request.POST)
				form2 = forms.form_empDetailForm(request.POST)
				print(form1.errors)
				print(form2.errors)
				if form1.is_valid() and form2.is_valid():

					sendme = User.objects.get(username=request.user)

					obj = form2.save(commit=False)
					obj.info = request.user
					obj.save()

					sendme.doc_link  = 	form1.cleaned_data['doc_link']
					sendme.save()

					return HttpResponseRedirect("/associate_form2/")
			return render(request,'associate_form1.html',{'form1':form1,'form2':form2,'info':data_final})
		return render(request,'associate_form1.html',{'form1':form1,'form2':form2,'info':data_final})
	else:
		return HttpResponseRedirect('/invalid')

@login_required
def hod_form5(request):
	if request.user.is_hod():

		form6 = forms.form_conference()
		form7 = forms.form_journal()

		if conference.objects.filter(info=request.user).exists():

			return HttpResponseRedirect("/logout/")
		else:
			if request.method == 'POST':
				sendme = User.objects.get(username=request.user)
				form6 = forms.form_conference(request.POST)
				form7 = forms.form_journal(request.POST)
				if form6.is_valid() and form7.is_valid():
					obj3 = form6.save(commit=False)
					obj4 = form7.save(commit=False)
					obj3.info = request.user
					obj4.info = request.user

					obj3.save()
					obj4.save()

					if sendme.teach_status == False:
						sendme.teach_status = True
						sendme.save()
					return HttpResponseRedirect("/logout/")
			return render(request,'hod_form5.html',{'form6':form6,'form7':form7})
		return render(request,'hod_form5.html',{'form6':form6,'form7':form7})
	else:
		return HttpResponseRedirect('/invalid')

@login_required
def hod_form4(request):
	if request.user.is_hod():
		form5 = forms.form_remarks()
		if remarks.objects.filter(info=request.user).exists():

			return HttpResponseRedirect("/hod_form5/")
		else:
			if request.method == 'POST':
				form5 = forms.form_remarks(request.POST)
				if form5.is_valid():
					obj3 = form5.save(commit=False)
					obj3.info = request.user
					obj3.save()
					return HttpResponseRedirect("/hod_form5/")
			return render(request,'hod_form4.html',{'form5':form5})
		return render(request,'hod_form4.html',{'form5':form5})
	else:
		return HttpResponseRedirect('/invalid')

@login_required
def hod_form3(request):
	if request.user.is_hod():
		form4 = forms.form_rd()
		if rd.objects.filter(info=request.user).exists():

			return HttpResponseRedirect("/hod_form4/")
		else:
			if request.method == 'POST':
				form4 = forms.form_rd(request.POST)
				if form4.is_valid():
					obj2 = form4.save(commit=False)
					obj2.info = request.user
					obj2.save()
					return HttpResponseRedirect("/hod_form4/")
			return render(request,'hod_form3.html',{'form4':form4})
		return render(request,'hod_form3.html',{'form4':form4})
	else:
		return HttpResponseRedirect('/invalid')


@login_required
def hod_form2(request):
	if request.user.is_hod():
		form3 = forms.form_feedbackTab()

		if feedbackTab.objects.filter(info=request.user).exists():

			return HttpResponseRedirect("/hod_form3/")
		else:
			if request.method == 'POST':
				form3 = forms.form_feedbackTab(request.POST)
				if form3.is_valid():
					obj1 = form3.save(commit=False)
					obj1.info = request.user
					obj1.save()
					return HttpResponseRedirect("/hod_form3/")
			return render(request,'hod_form2.html',{'form3':form3})

		return render(request,'hod_form2.html',{'form3':form3})
	else:
		return HttpResponseRedirect('/invalid')



@login_required
def hod_form1(request):
	if request.user.is_hod():

		user = request.user
		print(user)
		data_final = User.objects.get(username=user)
		form1 = forms.form_User()
		form2 = forms.form_empDetailForm()

		if empDetailForm.objects.filter(info=user).exists():

			return HttpResponseRedirect("/hod_form2/")

		else:

			if request.method == 'POST':
				form1 = forms.form_User(request.POST)
				form2 = forms.form_empDetailForm(request.POST)


				if form1.is_valid() and form2.is_valid():

					sendme = User.objects.get(username=request.user)

					obj = form2.save(commit=False)
					obj.info = request.user
					obj.save()

					sendme.doc_link  = 	form1.cleaned_data['doc_link']
					sendme.save()

					return HttpResponseRedirect("/hod_form2/")
			return render(request,'hod_form1.html',{'form1':form1,'form2':form2,'info':data_final})
		return render(request,'hod_form1.html',{'form1':form1,'form2':form2,'info':data_final})

	else:
		return HttpResponseRedirect('/invalid')






@login_required
def assistant_preview(request):
	if request.user.is_assistant_professor():
		name = request.user
		data1 = User.objects.get(username=name)
		data2 = empDetailForm.objects.get(info=name);
		data3 = feedbackTab.objects.get(info=name);
		data4 = rd.objects.get(info=name);
		data5 = remarks.objects.get(info=name);
		data6 = conference.objects.get(info=name);
		data7 = journal.objects.get(info=name);


		context1 = {
		"key1":data1,
		"key2":data2,
		"key3":data3,
		"key4":data4,
		"key5":data5,
		"key6":data6,
		"key7":data7,

		}

		return render(request,'assistant_preview.html',context=context1)
	else:
		return HttpResponseRedirect('/invalid')


@login_required
def associate_preview(request):
	name = request.user
	data1 = User.objects.get(username=name)
	data2 = empDetailForm.objects.get(info=name);
	data3 = feedbackTab.objects.get(info=name);
	data4 = rd.objects.get(info=name);
	data5 = remarks.objects.get(info=name);
	data6 = conference.objects.get(info=name);
	data7 = journal.objects.get(info=name);

	context1 = {
	"key1":data1,
	"key2":data2,
	"key3":data3,
	"key4":data4,
	"key5":data5,
	"key6":data6,
	"key7":data7,
	}

	return render(request,'associate_preview.html',context=context1)

@login_required
def hod_preview(request):
	name = request.user
	data1 = User.objects.get(username=name)
	data2 = empDetailForm.objects.get(info=name);
	data3 = feedbackTab.objects.get(info=name);
	data4 = rd.objects.get(info=name);
	data5 = remarks.objects.get(info=name);
	data6 = conference.objects.get(info=name);
	data7 = journal.objects.get(info=name);

	context1 = {
	"key1":data1,
	"key2":data2,
	"key3":data3,
	"key4":data4,
	"key5":data5,
	"key6":data6,
	"key7":data7,

	}

	return render(request,'hod_preview.html',context=context1)
