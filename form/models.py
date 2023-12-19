from django.db import models
from django.utils.translation import gettext_lazy as _
import json

from django.contrib.auth.models import User


class Form(models.Model):
    title = models.CharField(max_length=100)
    active = models.BooleanField(default=1)

    def __str__(self):
        return self.title


class Field(models.Model):
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    order = models.IntegerField(blank=True, null=True)

    class TYPE(models.IntegerChoices):
        SELECT = 1, _('selection')
        COMMENT = 2, _('comment')
        Boolean = 3, _('Boolean')
        File = 4, _('File')

    type = models.IntegerField(choices=TYPE.choices, default=1)
    active = models.BooleanField(default=1)

    def __str__(self):
        return self.title + " - " + self.form.title


class Select(models.Model):
    field = models.ForeignKey(Field, related_name="items", on_delete=models.DO_NOTHING)
    value = models.CharField(max_length=100)

    def __str__(self):
        return self.value + " - " + self.field.title + " - " + self.field.form.title


class File(models.Model):
    field = models.ForeignKey(Field, on_delete=models.DO_NOTHING)
    value = models.URLField(blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.title + " - " + self.field.title + " - " + self.field.form.title


class Value(models.Model):
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
    value = models.CharField(blank=True, null=True, max_length=256)
    submitter = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    select_related_value = models.ForeignKey(Select, on_delete=models.SET_NULL, blank=True, null=True, related_name='related_values')
    file_related_value = models.ForeignKey(File, on_delete=models.SET_NULL, blank=True, null=True, related_name='related_values')



