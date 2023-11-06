# Generated by Django 4.2.5 on 2023-11-05 14:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Studio', '0002_alter_application_category_alter_application_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
