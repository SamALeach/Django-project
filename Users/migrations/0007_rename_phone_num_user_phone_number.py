# Generated by Django 4.0.2 on 2022-02-24 20:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0006_alter_user_role'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='phone_num',
            new_name='phone_number',
        ),
    ]
