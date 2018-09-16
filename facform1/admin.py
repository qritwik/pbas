from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources

from .models import *
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin


# Register your models here.



@admin.register(User)
class UserAdmin(DjangoUserAdmin, ImportExportModelAdmin):

	fieldsets = (
		(None, {'fields': ('username', 'email', 'password')}),
		(('Personal info'), {'fields': ('first_name', 'last_name', 'phone', 'department','info')}),
		(('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
									   )}),

		(('Status'), {'fields': ('teach_status','hod_status','principal_status')}),

		(('Designation'), {'fields': ('designation',)}),
		(('Important dates'), {'fields': ('last_login', 'date_joined')}),
	)

	list_display = ('username', 'first_name', 'last_name', 'phone', 'email')
	search_fields = ('email', 'first_name', 'last_name', 'username', 'phone')
	ordering = ('username',)

admin.site.register(empDetailForm)
admin.site.register(feedbackTab)
admin.site.register(rd)
admin.site.register(remarks)
admin.site.register(remarks1)
admin.site.register(remarks2)

admin.site.register(Designation)

admin.site.register(Department)
