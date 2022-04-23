# Generated by Django 3.2 on 2022-04-19 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onepico', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='prefix',
            field=models.IntegerField(choices=[('+353', '+34')], default=353),
        ),
        migrations.AlterField(
            model_name='booking',
            name='phone',
            field=models.IntegerField(),
        )
    ]
