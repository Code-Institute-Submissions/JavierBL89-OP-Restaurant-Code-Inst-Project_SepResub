# Generated by Django 3.2 on 2022-08-31 00:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20220830_1102'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='f_name',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='l_name',
            new_name='last_name',
        ),
    ]
