# Generated by Django 4.2.5 on 2023-10-02 09:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0002_customuser_name_alter_customuser_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='name',
        ),
    ]
