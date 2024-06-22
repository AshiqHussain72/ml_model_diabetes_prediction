# Generated by Django 4.0.3 on 2022-06-13 06:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('diabetes', '0004_alter_prediction_age_alter_prediction_blood_pressure_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prediction',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]