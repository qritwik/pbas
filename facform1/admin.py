from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources

from .models import *
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin


# Register your models here.

admin.site.site_header = "PBAS System";

# Register your models here.
class UserResource(resources.ModelResource):
	class Meta:
		model = User


@admin.register(User)
class UserAdmin(DjangoUserAdmin, ImportExportModelAdmin):

	fieldsets = (
		(None, {'fields': ('username', 'email', 'password')}),
		(('Personal info'), {'fields': ('first_name', 'last_name', 'phone', 'department','info')}),
		(('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
									   )}),

		(('Documents'), {'fields': ('doc_link',)}),

		(('Status'), {'fields': ('teach_status','hod_status','principal_status')}),

		(('Designation'), {'fields': ('designation',)}),
		(('Important dates'), {'fields': ('last_login', 'date_joined')}),
	)

	list_display = ('username', 'first_name', 'last_name', 'phone', 'email')
	search_fields = ('email', 'first_name', 'last_name', 'username', 'phone')
	ordering = ('username',)
	read_only = "password"
	resource_class = UserResource

class empDetailResource(resources.ModelResource):
	class Meta:
		model = empDetailForm


@admin.register(empDetailForm)
class UserempDetailForm(ImportExportModelAdmin):


	list_display = ('name',)
	search_fields = ('info__first_name',)
	ordering = ('id',)
	resource_class = empDetailResource

	def name(self, instance):
		return instance.info.first_name




# admin.site.register(empDetailForm)


class feedbackTabResource(resources.ModelResource):
	class Meta:
		model = feedbackTab


@admin.register(feedbackTab)
class UserfeedbackTab(ImportExportModelAdmin):


	list_display = ('name',)
	search_fields = ('info__first_name',)
	ordering = ('id',)
	resource_class = feedbackTabResource

	def name(self, instance):
		return instance.info.first_name

# admin.site.register(feedbackTab)
class rdResource(resources.ModelResource):
	class Meta:
		model = rd


@admin.register(rd)
class Userrd(ImportExportModelAdmin):


	list_display = ('name',)
	list_filter = ('info__department',)
	search_fields = ('info__first_name',)
	ordering = ('id',)
	resource_class = rdResource

	def name(self, instance):
		return instance.info.first_name


# admin.site.register(rd)

class remarksResource(resources.ModelResource):
	class Meta:
		model = remarks


@admin.register(remarks)
class Userremarks(ImportExportModelAdmin):


	list_display = ('name',)
	list_filter = ('info__department',)
	search_fields = ('info__first_name',)
	ordering = ('id',)
	resource_class = remarksResource

	def name(self, instance):
		return instance.info.first_name

# admin.site.register(remarks)
class remarks1Resource(resources.ModelResource):
	class Meta:
		model = remarks1


@admin.register(remarks1)
class Userremarks1(ImportExportModelAdmin):


	list_display = ('name',)
	list_filter = ('info__department',)
	search_fields = ('info__first_name',)
	ordering = ('id',)
	resource_class = remarks1Resource

	def name(self, instance):
		return instance.info.first_name

# admin.site.register(remarks1)

class remarks2Resource(resources.ModelResource):
	class Meta:
		model = remarks2


@admin.register(remarks2)
class Userremarks2(ImportExportModelAdmin):


	list_display = ('name',)
	list_filter = ('info__department',)
	search_fields = ('info__first_name',)
	ordering = ('id',)
	resource_class = remarks2Resource

	def name(self, instance):
		return instance.info.first_name

# admin.site.register(remarks2)

admin.site.register(Designation)

admin.site.register(Department)
admin.site.register(ipr_type)
admin.site.register(ipr_status)

class conferenceResource(resources.ModelResource):
	class Meta:
		model = conference


@admin.register(conference)
class Userconference(ImportExportModelAdmin):


	list_display = ('name',)
	list_filter = ('info__department',)
	search_fields = ('info__first_name',)
	ordering = ('id',)
	resource_class = conferenceResource

	def name(self, instance):
		return instance.info.first_name

# admin.site.register(conference)
class journalResource(resources.ModelResource):
	class Meta:
		model = journal


@admin.register(journal)
class Userjournal(ImportExportModelAdmin):


	list_display = ('name',)
	list_filter = ('info__department',)
	search_fields = ('info__first_name',)
	ordering = ('id',)
	resource_class = journalResource

	def name(self, instance):
		return instance.info.first_name

# admin.site.register(journal)
