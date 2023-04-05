from django.shortcuts import render
from rest_auth.registration.views import RegisterView
from rest_auth.views import LoginView
from django.contrib.auth import login
# Create your views here.


class UserRegisterView(RegisterView):
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        # 회원가입 성공 시 자동 로그인 처리
        user = self.perform_create(request)
        login(request, user)
        return response
