# Generated by Django 4.2.8 on 2023-12-18 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0007_value_file_related_value_value_select_related_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
