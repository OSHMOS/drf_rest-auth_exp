from django.urls import path, include
from .views import UserRegisterView

urlpatterns = [
    path('accounts/registration/', UserRegisterView.as_view()),
    path('accounts/', include('dj_rest_auth.urls')),
    # path('accounts/registration/', include('dj_rest_auth.registration.urls')),
]
