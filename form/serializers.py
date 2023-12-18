from rest_framework import serializers
from .models import Form, Field, Value, Select, File
from django.contrib.auth.models import User


class ValueSerializer(serializers.ModelSerializer):
    submitter = serializers.SerializerMethodField()

    def get_submitter(self, obj):
        return obj.submitter.username if obj.submitter else None

    class Meta:
        model = Value
        fields = ('id', 'field', 'value', 'submitter')


class SelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Select
        exclude = ('id', 'field')


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        exclude = ('id', 'field')


class FieldSerializer(serializers.ModelSerializer):
    values = ValueSerializer(many=True, read_only=True)
    selects = SelectSerializer(many=True, read_only=True)
    files = FileSerializer(many=True, read_only=True)

    class Meta:
        model = Field
        fields = ('id', 'title', 'order', 'type', 'active', 'values', 'selects', 'files')


class CombinedFormSerializer(serializers.ModelSerializer):
    fields = FieldSerializer(many=True, read_only=True)

    class Meta:
        model = Form
        fields = ('id', 'title', 'active', 'fields')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        fields = Field.objects.filter(form=instance).order_by('order')
        serialized_fields = FieldSerializer(fields, many=True).data

        for field_data in serialized_fields:
            field_id = field_data['id']
            field_type = field_data['type']

            values = Value.objects.filter(field=field_id)
            value_data = ValueSerializer(values, many=True).data
            field_data['values'] = value_data

            if field_type == Field.TYPE.SELECT:
                selects = Select.objects.filter(field=field_id)
                select_data = SelectSerializer(selects, many=True).data
                field_data['selects'] = select_data
            elif field_type == Field.TYPE.File:
                files = File.objects.filter(field=field_id)
                file_data = FileSerializer(files, many=True).data
                field_data['files'] = file_data

        data['fields'] = serialized_fields
        return data


class FieldValueSerializer(serializers.Serializer):
    field_id = serializers.IntegerField()
    value = serializers.CharField()
    submitter = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    def create(self, validated_data):
        field_id = validated_data['field_id']
        value = validated_data['value']
        submitter = validated_data['submitter']

        field = Field.objects.get(pk=field_id)
        value_instance, created = Value.objects.get_or_create(field=field, submitter=submitter)
        value_instance.value = value
        value_instance.save()

        return value_instance
