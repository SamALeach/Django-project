# Generated by Django 4.0.2 on 2022-02-22 22:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0002_alter_user_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='phone_number',
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_num',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(999999999)]),
        ),
    ]
