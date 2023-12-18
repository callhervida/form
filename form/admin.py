from django.contrib import admin

from .models import Form, Field, Value, Select, File


class FormAdmin(admin.ModelAdmin):
    list_display = ('title', 'active')
    search_fields = ('title',)
    ordering = ['title', ]


class FieldAdmin(admin.ModelAdmin):
    list_display = ('title', 'active', 'order', 'form')
    search_fields = ('title',)
    ordering = ['title', ]


class ValueAdmin(admin.ModelAdmin):
    list_display = ('field', 'value')
    search_fields = ('field',)
    ordering = ['field', ]


class SelectAdmin(admin.ModelAdmin):
    list_display = ('field', 'value')
    search_fields = ('field',)
    ordering = ['field', ]


class FileAdmin(admin.ModelAdmin):
    list_display = ('field', 'value')
    search_fields = ('field',)
    ordering = ['field', ]


admin.site.register(Form, FormAdmin)
admin.site.register(Field, FieldAdmin)
admin.site.register(Value, ValueAdmin)
admin.site.register(Select, SelectAdmin)
admin.site.register(File, FileAdmin)


