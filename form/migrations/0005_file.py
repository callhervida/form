# Generated by Django 4.2.8 on 2023-12-18 09:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0004_rename_selects_select_value_submitter'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FileField(blank=True, null=True, upload_to='')),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='form.field')),
            ],
        ),
    ]
