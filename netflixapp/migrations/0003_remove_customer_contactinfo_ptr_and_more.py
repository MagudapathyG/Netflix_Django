# Generated by Django 4.2.1 on 2023-06-01 10:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('netflixapp', '0002_contactinfo_customer_staff'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='contactinfo_ptr',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='contactinfo_ptr',
        ),
        migrations.DeleteModel(
            name='contactinfo',
        ),
        migrations.DeleteModel(
            name='customer',
        ),
        migrations.DeleteModel(
            name='staff',
        ),
    ]
