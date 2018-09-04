from django.contrib import admin
from import_export import resources
from facform1.models import empDetail,empDetailForm,feedbackTab,rd,remarks

# Register your models here.

class empres(resources.ModelResource):

    class Meta:
        model = empDetail

admin.site.register(empDetail)
admin.site.register(empDetailForm)
admin.site.register(feedbackTab)
admin.site.register(rd)
admin.site.register(remarks)

