# Generated by Django 3.2 on 2022-05-06 10:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('onepico', '0017_auto_20220506_1026'),
    ]

    operations = [
        migrations.CreateModel(
            name='TableDinner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table_number', models.IntegerField(default=0)),
                ('table_max_people', models.BigIntegerField(default=2)),
                ('booked_for', models.BigIntegerField(blank=True)),
                ('table_status', models.CharField(choices=[('pending', 'pending'), ('confirmed', 'confirmed'), ('rejected', 'rejected'), ('expired', 'expired')], default='pending', max_length=50)),
                ('customer_name', models.CharField(blank=True, max_length=50)),
                ('date', models.DateField(verbose_name='%Y-%m-%d')),
                ('start_time', models.TimeField(verbose_name='%H:%M')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('table_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_table_dinner', to='onepico.booking')),
            ],
        ),
        migrations.CreateModel(
            name='TableLunch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table_number', models.IntegerField(default=0)),
                ('table_max_people', models.BigIntegerField(default=2)),
                ('booked_for', models.BigIntegerField(blank=True)),
                ('table_status', models.CharField(choices=[('pending', 'pending'), ('confirmed', 'confirmed'), ('rejected', 'rejected'), ('expired', 'expired')], default='pending', max_length=50)),
                ('customer_name', models.CharField(blank=True, max_length=50)),
                ('date', models.DateField(verbose_name='%Y-%m-%d')),
                ('start_time', models.TimeField(verbose_name='%H:%M')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('table_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_table_lunch', to='onepico.booking')),
            ],
        ),
        migrations.DeleteModel(
            name='Dinner',
        ),
        migrations.DeleteModel(
            name='Lunch',
        ),
        migrations.DeleteModel(
            name='Table',
        ),
    ]
