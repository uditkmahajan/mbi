# Generated by Django 3.0.3 on 2020-04-09 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mycustomer', '0025_auto_20200408_2235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mycustomer',
            name='Profile',
            field=models.ImageField(default='customer/simple.jpg', upload_to='customer'),
        ),
    ]