# Generated by Django 3.0.3 on 2020-04-07 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Mycustomer', '0018_auto_20200407_1540'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homeloan',
            name='Area',
        ),
        migrations.RemoveField(
            model_name='homeloan',
            name='Employ',
        ),
        migrations.RemoveField(
            model_name='homeloan',
            name='Income',
        ),
        migrations.RemoveField(
            model_name='homeloan',
            name='Loan',
        ),
        migrations.RemoveField(
            model_name='homeloan',
            name='Number',
        ),
        migrations.RemoveField(
            model_name='homeloan',
            name='Status',
        ),
    ]