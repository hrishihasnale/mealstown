from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import (
    userMain
)


router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('login/', userMain.UserLogin.as_view()),
    path('send_otp/', userMain.SendOTP.as_view()),
    path('otp_verification/', userMain.OTPVerification.as_view()),
    path('register/', userMain.UserRegister.as_view()),
    path('users/list/', userMain.UserList.as_view())
]