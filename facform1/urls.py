from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.contrib.auth.views import login, logout
from . import forms
from django.conf import settings
from django.urls import path

app_name = 'facform1'

urlpatterns = [
    url(r'^$', views.login, name="login-username-view"),
    url(r'^login/', login,{'template_name': 'otp.html','authentication_form': forms.LoginForm}, name='login'),
    url(r'^logout/$', logout, {'template_name': 'success.html'}, name='logout'),
    url(r'^main/', views.decide_view, name="decide-view"),
    # url(r'^front/', views.front,name="front"),

    url(r'^invalid/',views.invalid,name="invalid"),

    #url(r'^undo/', views.teach_fun, name="teach_fun"),

    url(r'^report/(?P<dept>[\w\-]+)$',views.report,name="report"),
    path('first_page/',views.first_page,name='first_page'),
    path('ao_principal/',views.ao_principal,name='ao_principal'),

    url(r'^assistant_form1/(?P<y>[\w\-]+)$', views.f_assistant1,name="assistant_form1"),
    path('f_assistant_edit1/<slug:y>/',views.f_assistant_edit1,name="f_assistant_edit1"),
    path('f_assistant1_final/<slug:y>/',views.f_assistant1_final,name="f_assistant1_final"),
    url(r'^assistant_form2/(?P<y>[\w\-]+)$', views.f_assistant2,name="assistant_form2"),
    path('f_assistant2_final/<slug:y>/',views.f_assistant2_final,name="f_assistant2_final"),
    path('f_assistant_edit2/<slug:y>/',views.f_assistant_edit2,name="f_assistant_edit2"),
    url(r'^assistant_form3/(?P<y>[\w\-]+)$', views.f_assistant3,name="assistant_form3"),
    path('f_assistant_edit3/<slug:y>/',views.f_assistant_edit3,name="f_assistant_edit3"),
    path('f_assistant3_final/<slug:y>/',views.f_assistant3_final,name="f_assistant3_final"),
    url(r'^assistant_form4/(?P<y>[\w\-]+)$', views.f_assistant4,name="assistant_form4"),
    path('f_assistant_edit4/<slug:y>/',views.f_assistant_edit4,name="f_assistant_edit4"),
    path('f_assistant4_final/<slug:y>/',views.f_assistant4_final,name="f_assistant4_final"),
    url(r'^assistant_form5/(?P<y>[\w\-]+)$', views.f_assistant5,name="assistant_form5"),
    path('f_assistant_edit5/<slug:y>/',views.f_assistant_edit5,name="f_assistant_edit5"),
    path('f_assistant5_final/<slug:y>/',views.f_assistant5_final,name="f_assistant5_final"),
    path('assistant/status/<slug:y>',views.status,name="status"),
    url(r'^assistant_preview/(?P<y>[\w\-]+)$', views.assistant_preview,name="assistant_preview"),

    url(r'^associate_form1/(?P<y>[\w\-]+)$', views.f_associate1,name="associate_form1"),
    path('f_associate_edit1/<slug:y>/',views.f_associate_edit1,name="f_associate_edit1"),
    path('f_associate1_final/<slug:y>/',views.f_associate1_final,name="f_associate1_final"),
    url(r'^associate_form2/(?P<y>[\w\-]+)$', views.f_associate2,name="associate_form2"),
    path('f_associate_edit2/<slug:y>/',views.f_associate_edit2,name="f_associate_edit2"),
    path('f_associate2_final/<slug:y>/',views.f_associate2_final,name="f_associate2_final"),
    url(r'^associate_form3/(?P<y>[\w\-]+)$', views.f_associate3,name="associate_form3"),
    path('f_associate_edit3/<slug:y>/',views.f_associate_edit3,name="f_associate_edit3"),
    path('f_associate3_final/<slug:y>/',views.f_associate3_final,name="f_associate3_final"),
    url(r'^associate_form4/(?P<y>[\w\-]+)$', views.f_associate4,name="associate_form4"),
    path('f_associate_edit4/<slug:y>/',views.f_associate_edit4,name="f_associate_edit4"),
    path('f_associate4_final/<slug:y>/',views.f_associate4_final,name="f_associate4_final"),
    url(r'^associate_form5/(?P<y>[\w\-]+)$', views.f_associate5,name="associate_form5"),
    path('f_associate_edit5/<slug:y>/',views.f_associate_edit5,name="f_associate_edit5"),
    path('f_associate5_final/<slug:y>/',views.f_associate5_final,name="f_associate5_final"),

    url(r'^associate_preview/(?P<y>[\w\-]+)$', views.associate_preview,name="associate_preview"),


    url(r'^hod_form1/(?P<y>[\w\-]+)$', views.hod_form1,name="hod_form1"),
    path('hod_form1_final/<slug:y>/',views.hod_form1_final,name="hod_form1_final"),
    path('hod_form1_edit/<slug:y>/',views.hod_form1_edit,name="hod_form1_edit"),
    url(r'^hod_form2/(?P<y>[\w\-]+)$', views.hod_form2,name="hod_form2"),
    path('hod_form2_final/<slug:y>/',views.hod_form2_final,name="hod_form2_final"),
    path('hod_form2_edit/<slug:y>/',views.hod_form2_edit,name="hod_form2_edit"),
    url(r'^hod_form3/(?P<y>[\w\-]+)$', views.hod_form3,name="hod_form3"),
    path('hod_form3_final/<slug:y>/',views.hod_form3_final,name="hod_form3_final"),
    path('hod_form3_edit/<slug:y>/',views.hod_form3_edit,name="hod_form3_edit"),
    url(r'^hod_form4/(?P<y>[\w\-]+)$', views.hod_form4,name="hod_form4"),
    path('hod_form4_final/<slug:y>/',views.hod_form4_final,name="hod_form4_final"),
    path('hod_form4_edit/<slug:y>/',views.hod_form4_edit,name="hod_form4_edit"),
    url(r'^hod_form5/(?P<y>[\w\-]+)$', views.hod_form5,name="hod_form5"),
    path('hod_form5_final/<slug:y>/',views.hod_form5_final,name="hod_form5_final"),
    path('hod_form5_edit/<slug:y>/',views.hod_form5_edit,name="hod_form5_edit"),

    url(r'^hod_preview/(?P<y>[\w\-]+)$', views.hod_preview,name="hod_preview"),


    url(r'^hod_first/(?P<y>[\w\-]+)$', views.hod_first,name="hod_first"),
    url(r'^hod_display/(?P<y>[\w\-]+)$', views.hod_display,name="hod_display"),
    url(r'^hod_teacher_display/(?P<pk>[\w\-]+)/(?P<y>[\w\-]+)$', views.hod_teacher_display,name="hod_teacher_display"),
    url(r'^hod_teacher1_display/(?P<pk>[\w\-]+)/(?P<y>[\w\-]+)$', views.hod_teacher1_display,name="hod_teacher1_display"),

    url(r'^hod_teacher_display_edit/(?P<pk>[\w\-]+)/(?P<y>[\w\-]+)$', views.hod_teacher_display_edit,name="hod_teacher_display_edit"),
    url(r'^hod_teacher1_display_edit/(?P<pk>[\w\-]+)/(?P<y>[\w\-]+)$', views.hod_teacher1_display_edit,name="hod_teacher1_display_edit"),



    url(r'^principal_first/(?P<y>[\w\-]+)$', views.principal_first,name="principal_first"),
    url(r'^principal_display/(?P<dept>[\w\-]+)/(?P<y>[\w\-]+)$', views.principal_display,name="principal_display"),
    url(r'^principal_teacher_display/(?P<pk>[\w\-]+)/(?P<y>[\w\-]+)$', views.principal_teacher_display,name="principal_teacher_display"),
    url(r'^principal_teacher_display_edit/(?P<pk>[\w\-]+)/(?P<y>[\w\-]+)$', views.principal_teacher_display_edit,name="principal_teacher_display_edit"),

    url(r'^principal_teacher1_display/(?P<pk>[\w\-]+)/(?P<y>[\w\-]+)$', views.principal_teacher1_display,name="principal_teacher1_display"),
    url(r'^principal_teacher1_display_edit/(?P<pk>[\w\-]+)/(?P<y>[\w\-]+)$', views.principal_teacher1_display_edit,name="principal_teacher1_display_edit"),

    url(r'^principal_hod_display/(?P<pk>[\w\-]+)/(?P<y>[\w\-]+)$', views.principal_hod_display,name="principal_hod_display"),

    url(r'^principal_hod_display_edit/(?P<pk>[\w\-]+)/(?P<y>[\w\-]+)$', views.principal_hod_display_edit,name="principal_hod_display_edit"),





    url(r'^ao_first/(?P<y>[\w\-]+)$', views.ao_first,name="ao_first"),
    url(r'^ao_consolidated/', views.ao_consolidated,name="ao_consolidated"),
    url(r'^ao_display/(?P<dept>[\w\-]+)/(?P<y>[\w\-]+)$',views.ao_display,name="ao_display"),
    url(r'^ao_approved/(?P<dept>[\w\-]+)/(?P<y>[\w\-]+)$', views.ao_approved,name="ao_approved"),
    url(r'^ao_teacher_display/(?P<name>[\w\-\.\w]+)/(?P<y>[\w\-]+)$',views.ao_teacher_display,name="ao_teacher_display"),
    url(r'^ao_teacher1_display/(?P<name>[\w\-\.\w]+)/(?P<y>[\w\-]+)$',views.ao_teacher1_display,name="ao_teacher1_display"),
    url(r'^ao_hod_display/(?P<name>[\w\-\.\w]+)/(?P<y>[\w\-]+)$',views.ao_hod_display,name="ao_hod_display"),

 #    url(r'^success/', views.success,name="success"),
  ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
