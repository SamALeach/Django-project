# Generated by Django 4.0.2 on 2022-02-20 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phone_num', models.IntegerField()),
                ('email', models.CharField(max_length=50)),
                ('role', models.CharField(max_length=50)),
            ],
        ),
    ]
