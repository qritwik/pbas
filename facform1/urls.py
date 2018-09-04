from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/', views.login,name="login"),
    # url(r'^front/', views.front,name="front"),
    # url(r'^assistant_form/', views.f_assistant,name="assistant_form"),
    # url(r'^associate_form/', views.associate_form,name="associate_form"),
    url(r'^hod_form/', views.hod_form,name="hod_form"),
    url(r'^hod_first/', views.phone_otp,name="hod_first"),
    url(r'^hod_display/', views.hod_display,name="hod_display"),
    url(r'^principal_first/', views.principal_first,name="principal_first"),
    url(r'^principal_display/', views.principal_display,name="principal_display"),
    url(r'^success/', views.success,name="success"),
 ]
