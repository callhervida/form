from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from user.views import UserCreateAPIView


urlpatterns = [
    path('login/', obtain_auth_token, name='login'),
    path('register/', UserCreateAPIView.as_view(), name='user-register'),

]