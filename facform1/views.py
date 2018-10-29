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
from openpyxl import Workbook
from django.http import HttpResponse, HttpResponseRedirect
from openpyxl.writer.excel import save_virtual_workbook


from django.contrib.auth.decorators import login_required
from django.forms import formset_factory




def report(request,dept):

	data1 = rd.objects.filter(info__department__name=dept)
	data2 = journal.objects.filter(info__department__name=dept)
	data3 = conference.objects.filter(info__department__name=dept)

	book = Workbook()
	book.create_sheet('Rd')
	book.create_sheet('Journal')
	book.create_sheet('Conference')



	rd1 = book['Rd']
	journal1 = book['Journal']
	conference1 = book['Conference']


	#-------------------rd-------------------

	rd1['A1'] = "Name"
	rd1['B1'] = "Department"
	rd1['C1'] = "Designation"
	rd1['D1'] = "w_s_d"
	rd1['E1'] = "w_n_d"
	rd1['F1'] = "w_i_d"
	rd1['G1'] = "w_m"
	rd1['H1'] = "p_s_d"
	rd1['I1'] = "p_n_d"
	rd1['J1'] = "p_i_d"
	rd1['K1'] = "p_m"
	rd1['L1'] = "onl_course_c"
	rd1['M1'] = "onl_course_m"
	rd1['N1'] = "s_c_n"
	rd1['O1'] = "f_c_n"
	rd1['P1'] = "o_c_n"
	rd1['Q1'] = "s_c_m"
	rd1['R1'] = "f_c_m"
	rd1['S1'] = "o_c_m"
	rd1['T1'] = "s_j_n"
	rd1['U1'] = "f_j_n"
	rd1['V1'] = "o_j_n"
	rd1['W1'] = "s_j_m"
	rd1['X1'] = "f_j_m"
	rd1['Y1'] = "o_j_m"
	rd1['Z1'] = "book_i"
	rd1['AA1'] = "book_n"
	rd1['AB1'] = "book_ci"

	rd1['AC1'] = "book_cn"
	rd1['AD1'] = "book_ai"
	rd1['AE1'] = "book_nm"
	rd1['AF1'] = "book_m"
	rd1['AG1'] = "if_s"

	rd1['AH1'] = "if_f"

	rd1['AI1'] = "if_c"

	rd1['AJ1'] = "ef_s"

	rd1['AK1'] = "ef_f"

	rd1['AL1'] = "ef_c"

	rd1['AM1'] = "eef_s"

	rd1['AN1'] = "eef_f"

	rd1['AO1'] = "eef_c"

	rd1['AP1'] = "Cw_2"

	rd1['AQ1'] = "Cw_2_5"
	rd1['AR1'] = "Cw_5"


	rd1['AS1'] = "ipr_info"
	rd1['AT1'] = "rp_marks"
	rd1['AU1'] = "R&D TOTAL MARKS"









	for i,rx in zip(range(2,40),data1):

		info1 = rx.info

		data4 = User.objects.get(username=info1)



		rd1.cell(row = i, column = 1).value = data4.first_name
		rd1.cell(row = i, column = 2).value = data4.department.name
		rd1.cell(row = i, column = 3).value = data4.designation.name







		rd1.cell(row = i, column = 4).value = rx.w_s_d
		rd1.cell(row = i, column = 5).value = rx.w_n_d
		rd1.cell(row = i, column = 6).value = rx.w_i_d
		rd1.cell(row = i, column = 7).value = rx.w_m

		rd1.cell(row = i, column = 8).value = rx.p_s_d
		rd1.cell(row = i, column = 9).value = rx.p_n_d
		rd1.cell(row = i, column = 10).value = rx.p_i_d
		rd1.cell(row = i, column = 11).value = rx.p_m

		rd1.cell(row = i, column = 12).value = rx.onl_course_c
		rd1.cell(row = i, column = 13).value = rx.onl_course_m

		rd1.cell(row = i, column = 14).value = rx.s_c_n
		rd1.cell(row = i, column = 15).value = rx.f_c_n
		rd1.cell(row = i, column = 16).value = rx.o_c_n

		rd1.cell(row = i, column = 17).value = rx.s_c_m
		rd1.cell(row = i, column = 18).value = rx.f_c_m
		rd1.cell(row = i, column = 19).value = rx.o_c_m

		rd1.cell(row = i, column = 20).value = rx.s_j_n
		rd1.cell(row = i, column = 21).value = rx.f_j_n
		rd1.cell(row = i, column = 22).value = rx.o_j_n

		rd1.cell(row = i, column = 23).value = rx.s_j_m
		rd1.cell(row = i, column = 24).value = rx.f_j_m
		rd1.cell(row = i, column = 25).value = rx.o_j_m


		rd1.cell(row = i, column = 26).value = rx.book_i
		rd1.cell(row = i, column = 27).value = rx.book_n
		rd1.cell(row = i, column = 28).value = rx.book_ci
		rd1.cell(row = i, column = 29).value = rx.book_cn
		rd1.cell(row = i, column = 30).value = rx.book_ai
		rd1.cell(row = i, column = 31).value = rx.book_nm


		rd1.cell(row = i, column = 32).value = rx.book_m


		rd1.cell(row = i, column = 33).value = rx.if_s
		rd1.cell(row = i, column = 34).value = rx.if_f
		rd1.cell(row = i, column = 35).value = rx.if_c

		rd1.cell(row = i, column = 36).value = rx.ef_s
		rd1.cell(row = i, column = 37).value = rx.ef_f
		rd1.cell(row = i, column = 38).value = rx.ef_c


		rd1.cell(row = i, column = 39).value = rx.eef_s
		rd1.cell(row = i, column = 40).value = rx.eef_f
		rd1.cell(row = i, column = 41).value = rx.eef_c

		rd1.cell(row = i, column = 42).value = rx.Cw_2
		rd1.cell(row = i, column = 43).value = rx.Cw_2_5
		rd1.cell(row = i, column = 44).value = rx.Cw_5


		rd1.cell(row = i, column = 45).value = rx.ipr_info

		rd1.cell(row = i, column = 46).value = rx.rp_marks
		rd1.cell(row = i, column = 47).value = rx.rd_tot_marks







	journal1['A1'] = "Name"
	journal1['B1'] = "Department"
	journal1['C1'] = "Designation"

	journal1['D1'] = "j1_index"
	journal1['E1'] = "j1_name"
	journal1['F1'] = "j1_title"
	journal1['G1'] = "j1_volume"
	journal1['H1'] = "j1_issn"
	journal1['I1'] = "j1_date"
	journal1['J1'] = "j1_page"
	journal1['K1'] = "j1_author"

	journal1['L1'] = "j2_index"
	journal1['M1'] = "j2_name"
	journal1['N1'] = "j2_title"
	journal1['O1'] = "j2_volume"
	journal1['P1'] = "j2_issn"
	journal1['Q1'] = "j2_date"
	journal1['R1'] = "j2_page"
	journal1['S1'] = "j2_author"


	journal1['T1'] = "j3_index"
	journal1['U1'] = "j3_name"
	journal1['V1'] = "j3_title"
	journal1['W1'] = "j3_volume"
	journal1['X1'] = "j3_issn"
	journal1['Y1'] = "j3_date"
	journal1['Z1'] = "j3_page"
	journal1['AA1'] = "j3_author"



	journal1['AB1'] = "j4_index"
	journal1['AC1'] = "j4_name"
	journal1['AD1'] = "j4_title"
	journal1['AE1'] = "j4_volume"
	journal1['AF1'] = "j4_issn"
	journal1['AG1'] = "j4_date"
	journal1['AH1'] = "j4_page"
	journal1['AI1'] = "j4_author"


	journal1['AJ1'] = "j5_index"
	journal1['AK1'] = "j5_name"
	journal1['AL1'] = "j5_title"
	journal1['AM1'] = "j5_volume"
	journal1['AN1'] = "j5_issn"
	journal1['AO1'] = "j5_date"
	journal1['AP1'] = "j5_page"
	journal1['AQ1'] = "j5_author"



	journal1['AR1'] = "j6_index"
	journal1['AS1'] = "j6_name"
	journal1['AT1'] = "j6_title"
	journal1['AU1'] = "j6_volume"
	journal1['AV1'] = "j6_issn"
	journal1['AW1'] = "j6_date"
	journal1['AX1'] = "j6_page"
	journal1['AY1'] = "j6_author"


	journal1['AZ1'] = "j7_index"
	journal1['BA1'] = "j7_name"
	journal1['BB1'] = "j7_title"
	journal1['BC1'] = "j7_volume"
	journal1['BD1'] = "j7_issn"
	journal1['BE1'] = "j7_date"
	journal1['BF1'] = "j7_page"
	journal1['BG1'] = "j7_author"



	journal1['BH1'] = "j8_index"
	journal1['BI1'] = "j8_name"
	journal1['BJ1'] = "j8_title"
	journal1['BK1'] = "j8_volume"
	journal1['BL1'] = "j8_issn"
	journal1['BM1'] = "j8_date"
	journal1['BN1'] = "j8_page"
	journal1['BO1'] = "j8_author"



	for j,jx in zip(range(2,40),data2):

		info2 = jx.info

		data5 = User.objects.get(username=info2)

		journal1.cell(row = j, column = 1).value = data5.first_name
		journal1.cell(row = j, column = 2).value = data5.department.name
		journal1.cell(row = j, column = 3).value = data5.designation.name






		journal1.cell(row = j, column = 4).value = jx.j1_index
		journal1.cell(row = j, column = 5).value = jx.j1_name
		journal1.cell(row = j, column = 6).value = jx.j1_title
		journal1.cell(row = j, column = 7).value = jx.j1_volume
		journal1.cell(row = j, column = 8).value = jx.j1_issn
		journal1.cell(row = j, column = 9).value = jx.j1_date
		journal1.cell(row = j, column = 10).value = jx.j1_page
		journal1.cell(row = j, column = 11).value = jx.j1_author

		journal1.cell(row = j, column = 12).value = jx.j2_index
		journal1.cell(row = j, column = 13).value = jx.j2_name
		journal1.cell(row = j, column = 14).value = jx.j2_title
		journal1.cell(row = j, column = 15).value = jx.j2_volume
		journal1.cell(row = j, column = 16).value = jx.j2_issn
		journal1.cell(row = j, column = 17).value = jx.j2_date
		journal1.cell(row = j, column = 18).value = jx.j2_page
		journal1.cell(row = j, column = 19).value = jx.j2_author


		journal1.cell(row = j, column = 20).value = jx.j3_index
		journal1.cell(row = j, column = 21).value = jx.j3_name
		journal1.cell(row = j, column = 22).value = jx.j3_title
		journal1.cell(row = j, column = 23).value = jx.j3_volume
		journal1.cell(row = j, column = 24).value = jx.j3_issn
		journal1.cell(row = j, column = 25).value = jx.j3_date
		journal1.cell(row = j, column = 26).value = jx.j3_page
		journal1.cell(row = j, column = 27).value = jx.j3_author


		journal1.cell(row = j, column = 28).value = jx.j4_index
		journal1.cell(row = j, column = 29).value = jx.j4_name
		journal1.cell(row = j, column = 30).value = jx.j4_title
		journal1.cell(row = j, column = 31).value = jx.j4_volume
		journal1.cell(row = j, column = 32).value = jx.j4_issn
		journal1.cell(row = j, column = 33).value = jx.j4_date
		journal1.cell(row = j, column = 34).value = jx.j4_page
		journal1.cell(row = j, column = 35).value = jx.j4_author


		journal1.cell(row = j, column = 36).value = jx.j5_index
		journal1.cell(row = j, column = 37).value = jx.j5_name
		journal1.cell(row = j, column = 38).value = jx.j5_title
		journal1.cell(row = j, column = 39).value = jx.j5_volume
		journal1.cell(row = j, column = 40).value = jx.j5_issn
		journal1.cell(row = j, column = 41).value = jx.j5_date
		journal1.cell(row = j, column = 42).value = jx.j5_page
		journal1.cell(row = j, column = 43).value = jx.j5_author


		journal1.cell(row = j, column = 44).value = jx.j6_index
		journal1.cell(row = j, column = 45).value = jx.j6_name
		journal1.cell(row = j, column = 46).value = jx.j6_title
		journal1.cell(row = j, column = 47).value = jx.j6_volume
		journal1.cell(row = j, column = 48).value = jx.j6_issn
		journal1.cell(row = j, column = 49).value = jx.j6_date
		journal1.cell(row = j, column = 50).value = jx.j6_page
		journal1.cell(row = j, column = 51).value = jx.j6_author

		journal1.cell(row = j, column = 52).value = jx.j7_index
		journal1.cell(row = j, column = 53).value = jx.j7_name
		journal1.cell(row = j, column = 54).value = jx.j7_title
		journal1.cell(row = j, column = 55).value = jx.j7_volume
		journal1.cell(row = j, column = 56).value = jx.j7_issn
		journal1.cell(row = j, column = 57).value = jx.j7_date
		journal1.cell(row = j, column = 58).value = jx.j7_page
		journal1.cell(row = j, column = 59).value = jx.j7_author

		journal1.cell(row = j, column = 60).value = jx.j8_index
		journal1.cell(row = j, column = 61).value = jx.j8_name
		journal1.cell(row = j, column = 62).value = jx.j8_title
		journal1.cell(row = j, column = 63).value = jx.j8_volume
		journal1.cell(row = j, column = 64).value = jx.j8_issn
		journal1.cell(row = j, column = 65).value = jx.j8_date
		journal1.cell(row = j, column = 66).value = jx.j8_page
		journal1.cell(row = j, column = 67).value = jx.j8_author













	conference1['A1'] = "Name"
	conference1['B1'] = "Department"
	conference1['C1'] = "Designation"

	conference1['D1'] = "c1_name"
	conference1['E1'] = "c1_title"
	conference1['F1'] = "c1_place"
	conference1['G1'] = "c1_date"
	conference1['H1'] = "c1_index"
	conference1['I1'] = "c1_author"

	conference1['J1'] = "c2_name"
	conference1['K1'] = "c2_title"
	conference1['L1'] = "c2_place"
	conference1['M1'] = "c2_date"
	conference1['N1'] = "c2_index"
	conference1['O1'] = "c2_author"


	conference1['P1'] = "c3_name"
	conference1['Q1'] = "c3_title"
	conference1['R1'] = "c3_place"
	conference1['S1'] = "c3_date"
	conference1['T1'] = "c3_index"
	conference1['U1'] = "c3_author"


	conference1['V1'] = "c4_name"
	conference1['W1'] = "c4_title"
	conference1['X1'] = "c4_place"
	conference1['Y1'] = "c4_date"
	conference1['Z1'] = "c4_index"
	conference1['AA1'] = "c4_author"

	conference1['AB1'] = "c5_name"
	conference1['AC1'] = "c5_title"
	conference1['AD1'] = "c5_place"
	conference1['AE1'] = "c5_date"
	conference1['AF1'] = "c5_index"
	conference1['AG1'] = "c5_author"


	conference1['AH1'] = "c6_name"
	conference1['AI1'] = "c6_title"
	conference1['AJ1'] = "c6_place"
	conference1['AK1'] = "c6_date"
	conference1['AL1'] = "c6_index"
	conference1['AM1'] = "c6_author"

	conference1['AN1'] = "c7_name"
	conference1['AO1'] = "c7_title"
	conference1['AP1'] = "c7_place"
	conference1['AQ1'] = "c7_date"
	conference1['AR1'] = "c7_index"
	conference1['AS1'] = "c7_author"

	conference1['AT1'] = "c8_name"
	conference1['AU1'] = "c8_title"
	conference1['AV1'] = "c8_place"
	conference1['AW1'] = "c8_date"
	conference1['AX1'] = "c8_index"
	conference1['AY1'] = "c8_author"




	for k,cx in zip(range(2,40),data3):

		info3 = cx.info

		data6 = User.objects.get(username=info3)

		conference1.cell(row = k, column = 1).value = data6.first_name
		conference1.cell(row = k, column = 2).value = data6.department.name
		conference1.cell(row = k, column = 3).value = data6.designation.name






		conference1.cell(row = k, column = 4).value = cx.c1_index
		conference1.cell(row = k, column = 5).value = cx.c1_name
		conference1.cell(row = k, column = 6).value = cx.c1_place
		conference1.cell(row = k, column = 7).value = cx.c1_date
		conference1.cell(row = k, column = 8).value = cx.c1_index
		conference1.cell(row = k, column = 9).value = cx.c1_author


		conference1.cell(row = k, column = 10).value = cx.c2_index
		conference1.cell(row = k, column = 11).value = cx.c2_name
		conference1.cell(row = k, column = 12).value = cx.c2_place
		conference1.cell(row = k, column = 13).value = cx.c2_date
		conference1.cell(row = k, column = 14).value = cx.c2_index
		conference1.cell(row = k, column = 15).value = cx.c2_author


		conference1.cell(row = k, column = 16).value = cx.c3_index
		conference1.cell(row = k, column = 17).value = cx.c3_name
		conference1.cell(row = k, column = 18).value = cx.c3_place
		conference1.cell(row = k, column = 19).value = cx.c3_date
		conference1.cell(row = k, column = 20).value = cx.c3_index
		conference1.cell(row = k, column = 21).value = cx.c3_author


		conference1.cell(row = k, column = 22).value = cx.c4_index
		conference1.cell(row = k, column = 23).value = cx.c4_name
		conference1.cell(row = k, column = 24).value = cx.c4_place
		conference1.cell(row = k, column = 25).value = cx.c4_date
		conference1.cell(row = k, column = 26).value = cx.c4_index
		conference1.cell(row = k, column = 27).value = cx.c4_author


		conference1.cell(row = k, column = 28).value = cx.c5_index
		conference1.cell(row = k, column = 29).value = cx.c5_name
		conference1.cell(row = k, column = 30).value = cx.c5_place
		conference1.cell(row = k, column = 31).value = cx.c5_date
		conference1.cell(row = k, column = 32).value = cx.c5_index
		conference1.cell(row = k, column = 33).value = cx.c5_author

		conference1.cell(row = k, column = 34).value = cx.c6_index
		conference1.cell(row = k, column = 35).value = cx.c6_name
		conference1.cell(row = k, column = 36).value = cx.c6_place
		conference1.cell(row = k, column = 37).value = cx.c6_date
		conference1.cell(row = k, column = 38).value = cx.c6_index
		conference1.cell(row = k, column = 39).value = cx.c6_author


		conference1.cell(row = k, column = 40).value = cx.c7_index
		conference1.cell(row = k, column = 41).value = cx.c7_name
		conference1.cell(row = k, column = 42).value = cx.c7_place
		conference1.cell(row = k, column = 43).value = cx.c7_date
		conference1.cell(row = k, column = 44).value = cx.c7_index
		conference1.cell(row = k, column = 45).value = cx.c7_author


		conference1.cell(row = k, column = 46).value = cx.c8_index
		conference1.cell(row = k, column = 47).value = cx.c8_name
		conference1.cell(row = k, column = 48).value = cx.c8_place
		conference1.cell(row = k, column = 49).value = cx.c8_date
		conference1.cell(row = k, column = 50).value = cx.c8_index
		conference1.cell(row = k, column = 51).value = cx.c8_author
































































	response = HttpResponse(save_virtual_workbook(book), content_type='application/vnd.ms-excel')
	response['Content-Disposition'] = 'attachment; filename="final_report.xlsx"'
	return response











def ao_consolidated(request):

	data1 = User.objects.all().order_by('department')
	data2 = feedbackTab.objects.all().order_by('info__department')
	data3 = rd.objects.all().order_by('info__department')
	data4 = remarks1.objects.all().order_by('info__department')
	# data5 = remarks2.objects.all()

	print(data1.count())
	print(data2.count())
	print(data3.count())
	print(data4.count())



	data6 = zip(data1,data2,data3,data4)







	context = {
			'data1':data1,
			'data2':data2,
			'data3':data3,
			'data4':data4,
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
