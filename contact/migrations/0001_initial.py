# Generated by Django 3.2 on 2022-08-28 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_name', models.CharField(max_length=50)),
                ('contact_email', models.EmailField(max_length=100)),
                ('contact_comment', models.CharField(max_length=1000)),
            ],
        ),
    ]