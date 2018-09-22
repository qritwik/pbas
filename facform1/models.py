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

class ipr_type(models.Model):
	"""
	Description: Model Description
	"""
	name = models.CharField(max_length=40, blank=True, null=True)

	def __str__(self):
		return self.name


class ipr_status(models.Model):
	"""
	Description: Model Description
	"""
	name = models.CharField(max_length=40, blank=True, null=True)

	def __str__(self):
		return self.name

class author(models.Model):
	"""
	Description: Model Description
	"""
	name = models.CharField(max_length=100, blank=True, null=True)

	def __str__(self):
		return self.name		

class User(AbstractUser):
	phone = models.BigIntegerField(null=True)
	department = models.ForeignKey('Department', on_delete=models.CASCADE,null=True)
	designation = models.ForeignKey('Designation', on_delete=models.CASCADE,null=True)
	teach_status = models.BooleanField(default=False)
	hod_status = models.BooleanField(default=False)
	principal_status = models.BooleanField(default=False)
	doc_link = models.CharField(max_length=2000, blank=True, null=True)
	info = models.CharField(max_length=20, blank=True, null=True)


	def __str__(self):
		return self.username

	def is_assistant_professor(self):
		faculty = Designation.objects.get(pk=11)
		faculty1 = str(faculty)
		faculty2 = str(self.designation.name)
		if faculty1 == faculty2:
			return True
		return False

	def is_associate_professor(self):
		faculty = Designation.objects.get(pk=9)
		faculty1 = str(faculty)
		faculty2 = str(self.designation.name)
		if faculty1 == faculty2:
			return True
		return False

	def is_professor(self):
		faculty = Designation.objects.get(pk=10)
		faculty1 = str(faculty)
		faculty2 = str(self.designation.name)
		if faculty1 == faculty2:
			return True
		return False

	def is_hod(self):
		faculty = Designation.objects.get(pk=10)
		faculty1 = str(faculty)
		faculty2 = str(self.designation.name)
		if faculty1 == faculty2:
			return True
		return False

	def is_principal(self):
		faculty = Designation.objects.get(pk=7)
		faculty1 = str(faculty)
		faculty2 = str(self.designation.name)
		if faculty1 == faculty2:
			return True
		return False

	def is_ao(self):
		faculty = Designation.objects.get(pk=6)
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
	it_name = models.CharField(max_length=50, blank=True, null=True)
	it_f = models.DateField(blank=True, null=True)
	it_t = models.DateField(blank=True, null=True)

	high_qual = models.CharField(max_length=50,null=True)
	doj = models.DateField(null=True)
	# Present_pos = models.CharField(max_length=50,null=True,blank=True)
	Held_from = models.DateField(null=True)
	exp_teach = models.IntegerField(blank=True, null=True)
	exp_res = models.IntegerField( blank=True, null=True)
	exp_indus = models.IntegerField(blank=True, null=True)
	info = models.ForeignKey('User', on_delete=models.CASCADE,null=True)


#TABLE-3
class feedbackTab(models.Model):
	o_l1_name = models.CharField(max_length=100, blank=True, null=True)
	o_l1_f1 = models.CharField(max_length=100, blank=True, null=True)
	o_l1_f2 = models.CharField(max_length=100, blank=True, null=True)
	o_l1_favg = models.CharField(max_length=100, blank=True, null=True)

	o_l2_name =models.CharField(max_length=100, blank=True, null=True)
	o_l2_f1 = models.CharField(max_length=100, blank=True, null=True)
	o_l2_f2 = models.CharField(max_length=100, blank=True, null=True)
	o_l2_favg = models.CharField(max_length=100, blank=True, null=True)

	o_l3_name =models.CharField(max_length=100, blank=True, null=True)
	o_l3_f1 = models.CharField(max_length=100, blank=True, null=True)
	o_l3_f2 = models.CharField(max_length=100, blank=True, null=True)
	o_l3_favg = models.CharField(max_length=100, blank=True, null=True)


	o_l4_name = models.CharField(max_length=100, blank=True, null=True)
	o_l4_f1 = models.CharField(max_length=100, blank=True, null=True)
	o_l4_f2 = models.CharField(max_length=100, blank=True, null=True)
	o_l4_favg = models.CharField(max_length=100, blank=True, null=True)


	o_l5_name = models.CharField(max_length=100, blank=True, null=True)
	o_l5_f1 = models.CharField(max_length=100, blank=True, null=True)
	o_l5_f2 = models.CharField(max_length=100, blank=True, null=True)
	o_l5_favg = models.CharField(max_length=100, blank=True, null=True)

	o_l_f_avg = models.CharField(max_length=100, blank=True, null=True)


	o_t3_name = models.CharField(max_length=100, blank=True, null=True)
	o_t3_f1 = models.CharField(max_length=100, blank=True, null=True)
	o_t3_f2 = models.CharField(max_length=100, blank=True, null=True)
	o_t3_favg = models.CharField(max_length=100, blank=True, null=True)


	o_t2_name = models.CharField(max_length=100, blank=True, null=True)
	o_t2_f1 = models.CharField(max_length=100, blank=True, null=True)
	o_t2_f2 = models.CharField(max_length=100, blank=True, null=True)
	o_t2_favg = models.CharField(max_length=100, blank=True, null=True)


	o_t1_name = models.CharField(max_length=100, blank=True, null=True)
	o_t1_f1 = models.CharField(max_length=100, blank=True, null=True)
	o_t1_f2 = models.CharField(max_length=100, blank=True, null=True)
	o_t1_favg = models.CharField(max_length=100, blank=True, null=True)

	o_t_f_avg = models.CharField(max_length=100, blank=True, null=True)



	e_l1_name = models.CharField(max_length=100, blank=True, null=True)
	e_l1_f1 = models.CharField(max_length=100, blank=True, null=True)
	e_l1_f2 = models.CharField(max_length=100, blank=True, null=True)
	e_l1_favg = models.CharField(max_length=100, blank=True, null=True)


	e_l2_name = models.CharField(max_length=100, blank=True, null=True)
	e_l2_f1 = models.CharField(max_length=100, blank=True, null=True)
	e_l2_f2 = models.CharField(max_length=100, blank=True, null=True)
	e_l2_favg = models.CharField(max_length=100, blank=True, null=True)


	e_l3_name = models.CharField(max_length=100, blank=True, null=True)
	e_l3_f1 = models.CharField(max_length=100, blank=True, null=True)
	e_l3_f2 = models.CharField(max_length=100, blank=True, null=True)
	e_l3_favg = models.CharField(max_length=100, blank=True, null=True)


	e_l4_name = models.CharField(max_length=100, blank=True, null=True)
	e_l4_f1 = models.CharField(max_length=100, blank=True, null=True)
	e_l4_f2 = models.CharField(max_length=100, blank=True, null=True)
	e_l4_favg = models.CharField(max_length=100, blank=True, null=True)


	e_l5_name = models.CharField(max_length=100, blank=True, null=True)
	e_l5_f1 = models.CharField(max_length=100, blank=True, null=True)
	e_l5_f2 = models.CharField(max_length=100, blank=True, null=True)
	e_l5_favg = models.CharField(max_length=100, blank=True, null=True)

	e_l_f_avg = models.CharField(max_length=100, blank=True, null=True)



	e_t3_name = models.CharField(max_length=100, blank=True, null=True)
	e_t3_f1 = models.CharField(max_length=100, blank=True, null=True)
	e_t3_f2 = models.CharField(max_length=100, blank=True, null=True)
	e_t3_favg = models.CharField(max_length=100, blank=True, null=True)


	e_t2_name = models.CharField(max_length=100, blank=True, null=True)
	e_t2_f1 = models.CharField(max_length=100, blank=True, null=True)
	e_t2_f2 = models.CharField(max_length=100, blank=True, null=True)
	e_t2_favg = models.CharField(max_length=100, blank=True, null=True)


	e_t1_name = models.CharField(max_length=100, blank=True, null=True)
	e_t1_f1 = models.CharField(max_length=100, blank=True, null=True)
	e_t1_f2 = models.CharField(max_length=100, blank=True, null=True)
	e_t1_favg = models.CharField(max_length=100, blank=True, null=True)

	e_t_f_avg = models.CharField(max_length=100, blank=True, null=True)



	o_t1_stu_app = models.CharField(max_length=100, blank=True, null=True)
	o_t1_stu_pass = models.CharField(max_length=100, blank=True, null=True)
	o_t1_stu_perpass = models.CharField(max_length=100, blank=True, null=True)

	o_t2_stu_app = models.CharField(max_length=100, blank=True, null=True)
	o_t2_stu_pass = models.CharField(max_length=100, blank=True, null=True)
	o_t2_stu_perpass = models.CharField(max_length=100, blank=True, null=True)

	o_t3_stu_app = models.CharField(max_length=100, blank=True, null=True)
	o_t3_stu_pass = models.CharField(max_length=100, blank=True, null=True)
	o_t3_stu_perpass = models.CharField(max_length=100, blank=True, null=True)

	o_t_r_avg = models.CharField(max_length=100, blank=True, null=True)

	o_l1_stu_app = models.CharField(max_length=100, blank=True, null=True)
	o_l1_stu_pass = models.CharField(max_length=100, blank=True, null=True)
	o_l1_stu_perpass = models.CharField(max_length=100, blank=True, null=True)

	o_l2_stu_app = models.CharField(max_length=100, blank=True, null=True)
	o_l2_stu_pass = models.CharField(max_length=100, blank=True, null=True)
	o_l2_stu_perpass = models.CharField(max_length=100, blank=True, null=True)

	o_l3_stu_app = models.CharField(max_length=100, blank=True, null=True)
	o_l3_stu_pass = models.CharField(max_length=100, blank=True, null=True)
	o_l3_stu_perpass = models.CharField(max_length=100, blank=True, null=True)

	o_l4_stu_app = models.CharField(max_length=100, blank=True, null=True)
	o_l4_stu_pass = models.CharField(max_length=100, blank=True, null=True)
	o_l4_stu_perpass = models.CharField(max_length=100, blank=True, null=True)

	o_l5_stu_app = models.CharField(max_length=100, blank=True, null=True)
	o_l5_stu_pass = models.CharField(max_length=100, blank=True, null=True)
	o_l5_stu_perpass = models.CharField(max_length=100, blank=True, null=True)

	o_l_r_avg = models.CharField(max_length=100, blank=True, null=True)





	e_t1_stu_app = models.CharField(max_length=100, blank=True, null=True)
	e_t1_stu_pass = models.CharField(max_length=100, blank=True, null=True)
	e_t1_stu_perpass = models.CharField(max_length=100, blank=True, null=True)

	e_t2_stu_app = models.CharField(max_length=100, blank=True, null=True)
	e_t2_stu_pass = models.CharField(max_length=100, blank=True, null=True)
	e_t2_stu_perpass = models.CharField(max_length=100, blank=True, null=True)

	e_t3_stu_app = models.CharField(max_length=100, blank=True, null=True)
	e_t3_stu_pass = models.CharField(max_length=100, blank=True, null=True)
	e_t3_stu_perpass = models.CharField(max_length=100, blank=True, null=True)

	e_t_r_avg = models.CharField(max_length=100, blank=True, null=True)


	e_l1_stu_app = models.CharField(max_length=100, blank=True, null=True)
	e_l1_stu_pass = models.CharField(max_length=100, blank=True, null=True)
	e_l1_stu_perpass = models.CharField(max_length=100, blank=True, null=True)

	e_l2_stu_app = models.CharField(max_length=100, blank=True, null=True)
	e_l2_stu_pass = models.CharField(max_length=100, blank=True, null=True)
	e_l2_stu_perpass = models.CharField(max_length=100, blank=True, null=True)

	e_l3_stu_app = models.CharField(max_length=100, blank=True, null=True)
	e_l3_stu_pass = models.CharField(max_length=100, blank=True, null=True)
	e_l3_stu_perpass = models.CharField(max_length=100, blank=True, null=True)

	e_l4_stu_app = models.CharField(max_length=100, blank=True, null=True)
	e_l4_stu_pass = models.CharField(max_length=100, blank=True, null=True)
	e_l4_stu_perpass = models.CharField(max_length=100, blank=True, null=True)

	e_l5_stu_app = models.CharField(max_length=100, blank=True, null=True)
	e_l5_stu_pass = models.CharField(max_length=100, blank=True, null=True)
	e_l5_stu_perpass = models.CharField(max_length=100, blank=True, null=True)

	e_l_r_avg = models.CharField(max_length=100, blank=True, null=True)


	p1_name = models.CharField(max_length=100, blank=True, null=True)
	p1_f1 = models.CharField(max_length=100, blank=True, null=True)
	p1_f2 = models.CharField(max_length=100, blank=True, null=True)
	p1_favg = models.CharField(max_length=100, blank=True, null=True)

	p2_name = models.CharField(max_length=100, blank=True, null=True)
	p2_f1 = models.CharField(max_length=100, blank=True, null=True)
	p2_f2 = models.CharField(max_length=100, blank=True, null=True)
	p2_favg = models.CharField(max_length=100, blank=True, null=True)

	p3_name = models.CharField(max_length=100, blank=True, null=True)
	p3_f1 = models.CharField(max_length=100, blank=True, null=True)
	p3_f2 = models.CharField(max_length=100, blank=True, null=True)
	p3_favg = models.CharField(max_length=100, blank=True, null=True)

	p4_name = models.CharField(max_length=100, blank=True, null=True)
	p4_f1 = models.CharField(max_length=100, blank=True, null=True)
	p4_f2 = models.CharField(max_length=100, blank=True, null=True)
	p4_favg = models.CharField(max_length=100, blank=True, null=True)

	p5_name = models.CharField(max_length=100, blank=True, null=True)
	p5_f1 = models.CharField(max_length=100, blank=True, null=True)
	p5_f2 = models.CharField(max_length=100, blank=True, null=True)
	p5_favg = models.CharField(max_length=100, blank=True, null=True)

	p6_name = models.CharField(max_length=100, blank=True, null=True)
	p6_f1 = models.CharField(max_length=100, blank=True, null=True)
	p6_f2 = models.CharField(max_length=100, blank=True, null=True)
	p6_favg = models.CharField(max_length=100, blank=True, null=True)

	p7_name = models.CharField(max_length=100, blank=True, null=True)
	p7_f1 = models.CharField(max_length=100, blank=True, null=True)
	p7_f2 = models.CharField(max_length=100, blank=True, null=True)
	p7_favg = models.CharField(max_length=100, blank=True, null=True)

	p8_name = models.CharField(max_length=100, blank=True, null=True)
	p8_f1 = models.CharField(max_length=100, blank=True, null=True)
	p8_f2 = models.CharField(max_length=100, blank=True, null=True)
	p8_favg = models.CharField(max_length=100, blank=True, null=True)

	p9_name = models.CharField(max_length=100, blank=True, null=True)
	p9_f1 = models.CharField(max_length=100, blank=True, null=True)
	p9_f2 = models.CharField(max_length=100, blank=True, null=True)
	p9_favg = models.CharField(max_length=100, blank=True, null=True)

	p10_name = models.CharField(max_length=100, blank=True, null=True)
	p10_f1 = models.CharField(max_length=100, blank=True, null=True)
	p10_f2 = models.CharField(max_length=100, blank=True, null=True)
	p10_favg = models.CharField(max_length=100, blank=True, null=True)


	p_f_avg = models.CharField(max_length=100, blank=True, null=True)

	e_o_f_r_final = models.CharField(max_length=100, blank=True, null=True)

	info = models.ForeignKey('User', on_delete=models.CASCADE,null=True)



#TABLE-4
class rd(models.Model):
	w_s_d = models.IntegerField( blank=True, null=True)
	w_n_d = models.IntegerField( blank=True, null=True)
	w_i_d = models.IntegerField( blank=True, null=True)

	w_m = models.CharField(max_length=100, blank=True, null=True)

	p_s_d = models.IntegerField( blank=True, null=True)
	p_n_d = models.IntegerField( blank=True, null=True)
	p_i_d = models.IntegerField( blank=True, null=True)

	p_m = models.CharField(max_length=100, blank=True, null=True)

	onl_course_c = models.IntegerField( blank=True, null=True)

	onl_course_m = models.CharField(max_length=100, blank=True, null=True)

	s_c_m = models.CharField(max_length=100, blank=True, null=True)
	f_c_m = models.CharField(max_length=100, blank=True, null=True)
	o_c_m = models.CharField(max_length=100, blank=True, null=True)

	s_j_m = models.CharField(max_length=100, blank=True, null=True)
	f_j_m = models.CharField(max_length=100, blank=True, null=True)
	o_j_m = models.CharField(max_length=100, blank=True, null=True)

	book_i = models.IntegerField(blank=True, null=True)
	book_n = models.IntegerField( blank=True, null=True)
	book_ci = models.IntegerField(blank=True, null=True)
	book_cn = models.IntegerField(blank=True, null=True)
	book_ai = models.IntegerField( blank=True, null=True)
	book_nm = models.IntegerField( blank=True, null=True)

	book_m = models.CharField(max_length=100, blank=True, null=True)

	if_s = models.CharField(max_length=100, blank=True, null=True)
	if_f = models.CharField(max_length=100, blank=True, null=True)
	if_c = models.CharField(max_length=100, blank=True, null=True)

	ef_s = models.CharField(max_length=100, blank=True, null=True)
	ef_f = models.CharField(max_length=100, blank=True, null=True)
	ef_c = models.CharField(max_length=100, blank=True, null=True)

	eef_s = models.CharField(max_length=100, blank=True, null=True)
	eef_f = models.CharField(max_length=100, blank=True, null=True)
	eef_c = models.CharField(max_length=100, blank=True, null=True)

	Cw_2 = models.CharField(max_length=100, blank=True, null=True)
	Cw_2_5 = models.CharField(max_length=100, blank=True, null=True)
	Cw_5 = models.CharField(max_length=100, blank=True, null=True)

	ipr_status = models.ForeignKey('ipr_status', on_delete=models.CASCADE,null=True,blank=True)
	ipr_type = models.ForeignKey('ipr_type', on_delete=models.CASCADE,null=True,blank=True)
	ipr_info = models.TextField(blank=True, null=True)


	rp_marks = models.CharField(max_length=100, blank=True, null=True)

	rd_tot_marks = models.CharField(max_length=100, blank=True, null=True)



	info = models.ForeignKey('User', on_delete=models.CASCADE,null=True)


#TABLE-5
class remarks(models.Model):
	ta_ir = models.TextField( blank=True, null=True)
	ta_ic = models.TextField( blank=True, null=True)
	ta_dr = models.TextField( blank=True, null=True)
	info = models.ForeignKey('User', on_delete=models.CASCADE,null=True)


class conference(models.Model):

	c_name = models.CharField(max_length=100, blank=True, null=True)
	c_title = models.CharField(max_length=100, blank=True, null=True)
	c_place = models.CharField(max_length=100, blank=True, null=True)
	c_date = models.DateField(blank=True, null=True)
	c_index = models.CharField(max_length=100, blank=True, null=True)


	
	author = models.ForeignKey('author', on_delete=models.CASCADE,null=True)

	info = models.ForeignKey('User', on_delete=models.CASCADE,null=True)



class journal(models.Model):

	j_index = models.CharField(max_length=100, blank=True, null=True)
	j_name = models.CharField(max_length=100, blank=True, null=True)
	j_title = models.CharField(max_length=100, blank=True, null=True)
	j_volume = models.CharField(max_length=100, blank=True, null=True)
	j_issn = models.CharField(max_length=100, blank=True, null=True)
	j_date = models.DateField(blank=True, null=True)
	j_page = models.IntegerField( blank=True, null=True)


	

	author = models.ForeignKey('author', on_delete=models.CASCADE,null=True)

	info = models.ForeignKey('User', on_delete=models.CASCADE,null=True)


class remarks1(models.Model):
	hod_marks1 = models.IntegerField(blank=True, null=True)
	hod_marks2 = models.IntegerField( blank=True, null=True)
	ta_hod_remarks = models.TextField( blank=True, null=True)
	info = models.ForeignKey('User', on_delete=models.CASCADE,null=True)

class remarks2(models.Model):
	ta_prin_remarks = models.TextField( blank=True, null=True)
	ta_prin_remarks1 = models.TextField( blank=True, null=True)
	prin_marks1 = models.IntegerField( blank=True, null=True)
	prin_marks2 = models.IntegerField( blank=True, null=True)
	prin_marks3 = models.IntegerField( blank=True, null=True)
	total_marks = models.FloatField( blank=True, null=True)
	info = models.ForeignKey('User', on_delete=models.CASCADE,null=True)
	department = models.ForeignKey('Department', on_delete=models.CASCADE,null=True)



