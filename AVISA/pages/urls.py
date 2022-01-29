
from django.urls import path
from .views import BussinessFormView, BussinessView, JobFormView, JobView, LoginView, NotificationFormView, NotificationView, Register, home, logoutview, profileView,profileFormView, profile_single

urlpatterns=[
    path('profileform/',profileFormView,name='profile-form'),
    path('',home,name='home-page'),
    path('register/',Register,name="register-form"),
    path('login/',LoginView,name="login-page"),
    path('logout/',logoutview,name="logout-page"),
    path('profileview/',profileView,name="profileview-page"),
    path('jobform/',JobFormView,name="jobform-page"),
    path('bussiness_form/',BussinessFormView,name="bussiness-form"),
    path('notification_form/',NotificationFormView,name="notifiactionpage_form"),
    path('notification_view/',NotificationView,name="notifiaction-view"),
    path('bussiness_view/',BussinessView,name="bussiness_view"),
    path('jobs_view/',JobView,name="jobView-page"),
    path('profile_single/',profile_single,name="profile-single")

]