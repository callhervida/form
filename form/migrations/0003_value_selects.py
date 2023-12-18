# Generated by Django 4.2.8 on 2023-12-17 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0002_rename_form_field_form'),
    ]

    operations = [
        migrations.CreateModel(
            name='Value',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(blank=True, max_length=256, null=True)),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form.field')),
            ],
        ),
        migrations.CreateModel(
            name='Selects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=100)),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='items', to='form.field')),
            ],
        ),
    ]