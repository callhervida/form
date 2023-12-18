from django.urls import path
from . import views

urlpatterns = [
    # path('create/', views.FormCreateView.as_view(), name='form-create'),
    path('create/field/', views.FieldCreateView.as_view(), name='field-create'),
    path('list/<int:pk>/', views.CombinedFormView.as_view(), name='form-ordered-fields'),
    path('submit/<int:form_id>/', views.FillFormAPIView.as_view(), name='submit_form'),
]
