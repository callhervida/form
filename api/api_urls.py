from django.urls import path, include

urlpatterns = [
    path('form/', include('form.urls')),
]