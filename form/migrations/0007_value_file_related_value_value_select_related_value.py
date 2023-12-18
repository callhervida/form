# Generated by Django 4.2.8 on 2023-12-18 11:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0006_alter_field_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='value',
            name='file_related_value',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='related_values', to='form.file'),
        ),
        migrations.AddField(
            model_name='value',
            name='select_related_value',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='related_values', to='form.select'),
        ),
    ]
