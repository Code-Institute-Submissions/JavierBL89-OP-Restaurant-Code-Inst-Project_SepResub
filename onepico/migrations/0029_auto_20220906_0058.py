# Generated by Django 3.2 on 2022-09-06 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onepico', '0028_auto_20220905_2339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='excerpt',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='start_time',
            field=models.TimeField(choices=[(' ', 'Lunch'), ('12:00', '12:00'), ('12:15', '12:15'), ('12:30', '12:30'), ('12:45', '12:45'), ('13:00', '13:00'), ('13:15', '13:15'), ('13:30', '13:30'), ('13:45', '13:45'), ('14:00', '14:00'), ('14:15', '14:15'), ('14:30', '14:30'), (' ', 'Dinner'), ('18:00', '18:00'), ('18:00', '18:00'), ('18:15', '18:15'), ('18:30', '18:30'), ('18:45', '18:45'), ('19:00', '19:00'), ('19:15', '19:15'), ('19:30', '19:30'), ('19:45', '19:45'), ('19:30', '19:30'), ('19:45', '19:45'), ('20:00', '20:00'), ('20:15', '20:15'), ('20:30', '20:30'), ('20:45', '20:45'), ('21:00', '21:00'), ('21:15', '21:15'), ('21:30', '21:30')], default='12:00', verbose_name='%H:%M'),
        ),
    ]
