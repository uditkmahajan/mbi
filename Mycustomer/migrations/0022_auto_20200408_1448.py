# Generated by Django 3.0.3 on 2020-04-08 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mycustomer', '0021_homeloan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homeloan',
            name='loan_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]