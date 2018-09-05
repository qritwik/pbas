from django.db import models
from django.contrib.auth.models import AbstractUser, User

#TABLE-1

class Designation(models.Model):
	"""
	Description: Holds the Designations avbailable
	"""
	name = models.CharField(max_length=20, blank=True, null=True)
	
	def __str__(self):
		return self.name

class Department(models.Model):
	"""
	Description: Model Description
	"""
	name = models.CharField(max_length=20, blank=True, null=True)

	def __str__(self):
		return self.name

class User(AbstractUser):
	phone = models.BigIntegerField(null=True)
	department = models.ForeignKey('Department', on_delete=models.CASCADE,null=True)
	emp_id = models.IntegerField(blank=True, null=True)
	designation = models.ForeignKey('Designation', on_delete=models.CASCADE,null=True)
	
	def __str__(self):
		return self.username

	def is_assistant_professor(self):
		faculty = Designation.objects.get(name="assistant")
		faculty1 = str(faculty)
		faculty2 = str(self.designation.name)
		if faculty1 == faculty2:
			return True
		return False

	def is_associate_professor(self):
		faculty = Designation.objects.get(name="associate")
		faculty1 = str(faculty)
		faculty2 = str(self.designation.name)
		if faculty1 == faculty2:
			return True
		return False

	def is_hod(self):
		faculty = Designation.objects.get(name="HOD")
		faculty1 = str(faculty)
		faculty2 = str(self.designation.name)
		if faculty1 == faculty2:
			return True
		return False

	def is_principal(self):
		faculty = Designation.objects.get(name="Principal")
		faculty1 = str(faculty)
		faculty2 = str(self.designation.name)
		if faculty1 == faculty2:
			return True
		return False

	def is_ao(self):
		faculty = Designation.objects.get(name="AO")
		faculty1 = str(faculty)
		faculty2 = str(self.designation.name)
		if faculty1 == faculty2:
			return True
		return False

	def get_designation(self):
		return self.designation.name
	#get entry using form
#TABLE-2
class empDetailForm(models.Model):
	it_name = models.CharField(max_length=50,null=True)
	it_f = models.DateField(null=True)
	it_t = models.DateField(null=True)
	
	high_qual = models.CharField(max_length=50,null=True)
	doj = models.DateField(null=True)
	Present_pos = models.CharField(max_length=50,null=True)
	Held_from = models.DateField(null=True)
	exp_teach = models.IntegerField(null=True)
	exp_res = models.IntegerField(null=True)
	exp_indus = models.IntegerField(null=True)
	emp_id = models.ForeignKey('User', on_delete=models.CASCADE,null=True)


#TABLE-3
class feedbackTab(models.Model):
	o_l1_name = models.CharField(max_length=30)
	o_l1_f1 = models.CharField(max_length=30)
	o_l1_f2 = models.CharField(max_length=30)
	o_l1_favg = models.CharField(max_length=30)

	o_l2_name =models.CharField(max_length=30)
	o_l2_f1 = models.CharField(max_length=30)
	o_l2_f2 = models.CharField(max_length=30)
	o_l2_favg = models.CharField(max_length=30)

	o_l3_name =models.CharField(max_length=30)
	o_l3_f1 = models.CharField(max_length=30)
	o_l3_f2 = models.CharField(max_length=30)
	o_l3_favg = models.CharField(max_length=30)


	o_l4_name = models.CharField(max_length=30)
	o_l4_f1 = models.CharField(max_length=30)
	o_l4_f2 = models.CharField(max_length=30)
	o_l4_favg = models.CharField(max_length=30)


	o_l5_name = models.CharField(max_length=30)
	o_l5_f1 = models.CharField(max_length=30)
	o_l5_f2 = models.CharField(max_length=30)
	o_l5_favg = models.CharField(max_length=30)


	o_t3_name = models.CharField(max_length=30)
	o_t3_f1 = models.CharField(max_length=30)
	o_t3_f2 = models.CharField(max_length=30)
	o_t3_favg = models.CharField(max_length=30)


	o_t2_name = models.CharField(max_length=30)
	o_t2_f1 = models.CharField(max_length=30)
	o_t2_f2 = models.CharField(max_length=30)
	o_t2_favg = models.CharField(max_length=30)


	o_t1_name = models.CharField(max_length=30)
	o_t1_f1 = models.CharField(max_length=30)
	o_t1_f2 = models.CharField(max_length=30)
	o_t1_favg = models.CharField(max_length=30)


	e_l1_name = models.CharField(max_length=30)
	e_l1_f1 = models.CharField(max_length=30)
	e_l1_f2 = models.CharField(max_length=30)
	e_l1_favg = models.CharField(max_length=30)


	e_l2_name = models.CharField(max_length=30)
	e_l2_f1 = models.CharField(max_length=30)
	e_l2_f2 = models.CharField(max_length=30)
	e_l2_favg = models.CharField(max_length=30)


	e_l3_name = models.CharField(max_length=30)
	e_l3_f1 = models.CharField(max_length=30)
	e_l3_f2 = models.CharField(max_length=30)
	e_l3_favg = models.CharField(max_length=30)


	e_l4_name = models.CharField(max_length=30)
	e_l4_f1 = models.CharField(max_length=30)
	e_l4_f2 = models.CharField(max_length=30)
	e_l4_favg = models.CharField(max_length=30)


	e_l5_name = models.CharField(max_length=30)
	e_l5_f1 = models.CharField(max_length=30)
	e_l5_f2 = models.CharField(max_length=30)
	e_l5_favg = models.CharField(max_length=30)


	e_t3_name = models.CharField(max_length=30)
	e_t3_f1 = models.CharField(max_length=30)
	e_t3_f2 = models.CharField(max_length=30)
	e_t3_favg = models.CharField(max_length=30)


	e_t2_name = models.CharField(max_length=30)
	e_t2_f1 = models.CharField(max_length=30)
	e_t2_f2 = models.CharField(max_length=30)
	e_t2_favg = models.CharField(max_length=30)


	e_t1_name = models.CharField(max_length=30)
	e_t1_f1 = models.CharField(max_length=30)
	e_t1_f2 = models.CharField(max_length=30)
	e_t1_favg = models.CharField(max_length=30)


	o_t1_stu_app = models.CharField(max_length=30)
	o_t1_stu_pass = models.CharField(max_length=30)
	o_t1_stu_perpass = models.CharField(max_length=30)

	o_t2_stu_app = models.CharField(max_length=30)
	o_t2_stu_pass = models.CharField(max_length=30)
	o_t2_stu_perpass = models.CharField(max_length=30)

	o_t3_stu_app = models.CharField(max_length=30)
	o_t3_stu_pass = models.CharField(max_length=30)
	o_t3_stu_perpass = models.CharField(max_length=30)

	o_l1_stu_app = models.CharField(max_length=30)
	o_l1_stu_pass = models.CharField(max_length=30)
	o_l1_stu_perpass = models.CharField(max_length=30)

	o_l2_stu_app = models.CharField(max_length=30)
	o_l2_stu_pass = models.CharField(max_length=30)
	o_l2_stu_perpass = models.CharField(max_length=30)

	o_l3_stu_app = models.CharField(max_length=30)
	o_l3_stu_pass = models.CharField(max_length=30)
	o_l3_stu_perpass = models.CharField(max_length=30)

	o_l4_stu_app = models.CharField(max_length=30)
	o_l4_stu_pass = models.CharField(max_length=30)
	o_t4_stu_perpass = models.CharField(max_length=30)

	o_l5_stu_app = models.CharField(max_length=30)
	o_l5_stu_pass = models.CharField(max_length=30)
	o_l5_stu_perpass = models.CharField(max_length=30)




	e_t1_stu_app = models.CharField(max_length=30)
	e_t1_stu_pass = models.CharField(max_length=30)
	e_t1_stu_perpass = models.CharField(max_length=30)

	e_t2_stu_app = models.CharField(max_length=30)
	e_t2_stu_pass = models.CharField(max_length=30)
	e_t2_stu_perpass = models.CharField(max_length=30)

	e_t3_stu_app = models.CharField(max_length=30)
	e_t3_stu_pass = models.CharField(max_length=30)
	e_t3_stu_perpass = models.CharField(max_length=30)

	e_l1_stu_app = models.CharField(max_length=30)
	e_l1_stu_pass = models.CharField(max_length=30)
	e_l1_stu_perpass = models.CharField(max_length=30)

	e_l2_stu_app = models.CharField(max_length=30)
	e_l2_stu_pass = models.CharField(max_length=30)
	e_l2_stu_perpass = models.CharField(max_length=30)

	e_l3_stu_app = models.CharField(max_length=30)
	e_l3_stu_pass = models.CharField(max_length=30)
	e_l3_stu_perpass = models.CharField(max_length=30)

	e_l4_stu_app = models.CharField(max_length=30)
	e_l4_stu_pass = models.CharField(max_length=30)
	e_t4_stu_perpass = models.CharField(max_length=30)
	e_l5_stu_app = models.CharField(max_length=30)
	e_l5_stu_pass = models.CharField(max_length=30)
	e_l5_stu_perpass = models.CharField(max_length=30)

	p1_name = models.CharField(max_length=30)
	p1_f1 = models.CharField(max_length=30)
	p1_f2 = models.CharField(max_length=30)
	p1_favg = models.CharField(max_length=30)

	p2_name = models.CharField(max_length=30)
	p2_f1 = models.CharField(max_length=30)
	p2_f2 = models.CharField(max_length=30)
	p2_favg = models.CharField(max_length=30)
	emp_id = models.ForeignKey('User', on_delete=models.CASCADE,null=True)



#TABLE-4
class rd(models.Model):
	w_s_d = models.IntegerField()
	w_n_d = models.IntegerField()
	w_i_d = models.IntegerField()

	p_s_d = models.IntegerField()
	p_n_d = models.IntegerField()
	p_i_d = models.IntegerField()

	onl_course_c = models.IntegerField()

	j_index = models.CharField(max_length=30)
	j_name = models.CharField(max_length=30)
	j_title = models.CharField(max_length=30)
	j_volume = models.CharField(max_length=30)
	j_issn = models.CharField(max_length=30)
	j_date = models.DateField()
	j_page = models.IntegerField()

	c_name = models.CharField(max_length=30)
	c_title = models.CharField(max_length=30)
	c_place = models.CharField(max_length=30)
	c_date = models.DateField()
	c_index = models.CharField(max_length=30)

	book_i = models.IntegerField()
	book_n = models.IntegerField()
	book_ci = models.IntegerField()
	book_cn = models.IntegerField()
	book_ai = models.IntegerField()
	book_nm = models.IntegerField()

	if_s = models.CharField(max_length=30)
	if_f = models.CharField(max_length=30)
	if_c = models.CharField(max_length=30)

	ef_s = models.CharField(max_length=30)
	ef_f = models.CharField(max_length=30)
	ef_c = models.CharField(max_length=30)

	eef_s = models.CharField(max_length=30)
	eef_f = models.CharField(max_length=30)
	eef_c = models.CharField(max_length=30)

	Cw_2 = models.CharField(max_length=30)
	Cw_2_5 = models.CharField(max_length=30)
	Cw_5 = models.CharField(max_length=30)
	emp_id = models.ForeignKey('User', on_delete=models.CASCADE,null=True)



#TABLE-5
class remarks(models.Model):
	ta_ir = models.TextField()
	ta_ic = models.TextField()
	ta_dr = models.TextField()
	hod_marks1 = models.IntegerField()
	hod_marks2 = models.IntegerField()
	ta_hod_remarks = models.TextField()
	ta_prin_remarks = models.TextField()
	prin_marks1 = models.IntegerField()
	prin_marks2 = models.IntegerField()
	tot_marks = models.IntegerField()
	teach_status = models.BooleanField(default=False)
	hod_status = models.BooleanField(default=False)
	principal_status = models.BooleanField(default=False)
	emp_id = models.ForeignKey('User', on_delete=models.CASCADE,null=True)



	


	

# O_Theory_1
# O_Theory_2
# O_Theory_3
# O_T1_f1
# O_T1_f2
# O_T2_f1
# O_T2_f2
# O_T3_f1
# O_T3_f2

# O_T1_F_avg
# O_T2_F_avg
# O_T3_F_avg
# O_T1_app

# O_T2_app
# O_T3_app

# O_T1_pass
# O_T2_pass
# O_T3_pass

# O_T1_%
# O_T2_%
# O_T3_%

# O_L1
# O_L2
# O_L3
# O_L4
# O_L5

# O_L1_f1
# O_L1_f2
# O_L2_f1
# O_L2_f2
# O_L3_f1
# O_L3_f2
# O_L4_f1
# O_L4_f2
# O_L5_f1
# O_L5_f2

# O_L1_F_avg
# O_L2_F_avg
# O_L3_F_avg
# O_L4_F_avg
# O_L5_F_avg

# O_L1_app
# O_L2_app
# O_L3_app
# O_L4_app
# O_L5_app

# O_L1_pass
# O_L2_pass
# O_L3_pass
# O_L4_pass
# O_L5_pass

# O_L1_%
# O_L2_%
# O_L3_%
# O_L4_%
# O_L5_%

# E_Theory_1
# E_Theory_2
# E_Theory_3
# E_T1_f1
# E_T1_f2
# E_T2_f1
# E_T2_f2
# E_T3_f1
# E_T3_f2

# E_T1_F_avg
# E_T2_F_avg
# E_T3_F_avg
# E_T1_app

# E_T2_app
# E_T3_app

# E_T1_pass
# E_T2_pass
# E_T3_pass

# E_T1_%
# E_T2_%
# E_T3_%

# E_L1
# E_L2
# E_L3
# E_L4
# E_L5

# E_L1_f1
# E_L1_f2
# E_L2_f1
# E_L2_f2
# E_L3_f1
# E_L3_f2
# E_L4_f1
# E_L4_f2
# E_L5_f1
# E_L5_f2

# E_L1_F_avg
# E_L2_F_avg
# E_L3_F_avg
# E_L4_F_avg
# E_L5_F_avg

# E_L1_app
# E_L2_app
# E_L3_app
# E_L4_app
# E_L5_app

# E_L1_pass
# E_L2_pass
# E_L3_pass
# E_L4_pass
# E_L5_pass

# E_L1_%
# E_L2_%
# E_L3_%
# E_L4_%
# E_L5_%

# Project1_name
# Project2_name
# P1_f1
# P1_f2
# P2_f1
# P2_f2

# W_S
# W_N
# W_I

# P_S
# P_N 
# P_I

# Online_Course

# Pu_sa
# Pu_fs
# Pu_oa

# Jp_sa
# Jp_fs
# Jp_oa

# Book_I
# Book_N
# Book_Ci
# Book_Cn
# Book_Ai
# Book_Nm

# If_S
# If_Pi
# If_ci

# Ef_S
# Ef_Pi
# Ef_ci

# Eef_S
# Eef_Pi
# Eef_ci

# Cw_2
# Cw_2_5
# Cw_5

# #textarea
# Inno_contri

# Hod_marks_1

# #textarea
# Dept_respo

# Hod_marks_2

# #textarea
# Remarks_hod

# #textarea
# Inst_respo

# Principal_marks


# Total_marks









