# Generated by Django 4.2.8 on 2023-12-17 14:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('form', '0003_value_selects'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Selects',
            new_name='Select',
        ),
        migrations.AddField(
            model_name='value',
            name='submitter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
