from django.urls import path, include

urlpatterns = [
    path('form/', include('form.urls')),
    path('user/', include('user.urls')),
]