from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.permissions import IsAuthenticated

from .models import Form, Field, Value
from .serializers import CombinedFormSerializer, FieldSerializer, ValueSerializer, \
    FieldValueSerializer
from rest_framework import status


# class FormCreateView(generics.CreateAPIView):
#     queryset = Form.objects.all()
#     serializer_class = FormSerializer


class FieldCreateView(generics.CreateAPIView):
    queryset = Field.objects.all()
    serializer_class = FieldSerializer


class CombinedFormView(generics.ListAPIView):
    serializer_class = CombinedFormSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        submitter_id = self.request.user.id
        if submitter_id:
            return Form.objects.filter(field__value__submitter_id=submitter_id).distinct()
        return Form.objects.none()


class FillFormAPIView(APIView):

    def post(self, request, form_id):
        try:
            form = Form.objects.get(pk=form_id)
            data = request.data.get('fields', [])

            for field_data in data:
                field_id = field_data.get('field_id')
                value = field_data.get('value')

                field = Field.objects.get(pk=field_id, form=form)
                field_value, created = Value.objects.get_or_create(field=field, submitter=request.user)
                field_value.value = value
                field_value.save()

            return Response({'success': True}, status=status.HTTP_200_OK)
        except (Form.DoesNotExist, Field.DoesNotExist) as e:
            return Response({'success': False, 'error': str(e)}, status=status.HTTP_404_NOT_FOUND)