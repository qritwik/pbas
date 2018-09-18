from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout
from . import forms

urlpatterns = [
    url(r'^$', views.login, name="login-username-view"),
    url(r'^login/', login, {'template_name': 'otp.html','authentication_form': forms.LoginForm}, name='login'),
    url(r'^logout/$', logout, {'template_name': 'success.html'}, name='logout'),
    url(r'^main/', views.decide_view, name="decide-view"),
    # url(r'^front/', views.front,name="front"),
    url(r'^assistant_form/', views.f_assistant,name="assistant_form"),
    url(r'^associate_form/', views.f_associate,name="associate_form"),
    url(r'^hod_form/', views.hod_form,name="hod_form"),
    url(r'^hod_first/', views.hod_first,name="hod_first"),
    url(r'^hod_display/', views.hod_display,name="hod_display"),
    url(r'^hod_teacher_display/(?P<pk>[\w\-]+)$', views.hod_teacher_display,name="hod_teacher_display"),
    url(r'^hod_teacher1_display/(?P<pk>[\w\-]+)$', views.hod_teacher1_display,name="hod_teacher1_display"),
    
    url(r'^principal_first/', views.principal_first,name="principal_first"),
    url(r'^principal_display/(?P<dept>[\w\-]+)$', views.principal_display,name="principal_display"),
    url(r'^principal_teacher_display/(?P<pk>[\w\-]+)$', views.principal_teacher_display,name="principal_teacher_display"),
    url(r'^principal_teacher1_display/(?P<pk>[\w\-]+)$', views.principal_teacher1_display,name="principal_teacher1_display"),
    url(r'^principal_hod_display/(?P<pk>[\w\-]+)$', views.principal_hod_display,name="principal_hod_display"),
    

    url(r'^ao_first/', views.ao_first,name="ao_first"),
    url(r'^ao_display/(?P<dept>[\w\-]+)$', views.ao_display,name="ao_display"),
    url(r'^ao_teacher_display/(?P<name>[\w\-]+)$',views.ao_teacher_display,name="ao_teacher_display"),
    url(r'^ao_teacher1_display/(?P<name>[\w\-]+)$',views.ao_teacher1_display,name="ao_teacher1_display"),
    url(r'^ao_hod_display/(?P<name>[\w\-]+)$',views.ao_hod_display,name="ao_hod_display"),

 #    url(r'^success/', views.success,name="success"),
  ]
