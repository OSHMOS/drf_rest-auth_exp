from django.shortcuts import render
from rest_auth.registration.views import RegisterView
from rest_auth.views import LoginView
from django.contrib.auth import login
from rest_framework import status
# Create your views here.


class UserRegisterView(RegisterView):
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        if response.status_code == status.HTTP_201_CREATED:
            # 회원가입 성공 시 자동으로 로그인
            user = response.data.get('user')
            token = response.data.get('token')
            if user and token:
                user_auth = self.serializer_class(user).data
                user_auth['token'] = token
                response.data = user_auth
        return response
