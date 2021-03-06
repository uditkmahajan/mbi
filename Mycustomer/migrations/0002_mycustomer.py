# Generated by Django 3.0.3 on 2020-04-02 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mycustomer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyCustomer',
            fields=[
                ('s_no', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(default='', max_length=30)),
                ('Email', models.CharField(default='', max_length=40)),
                ('Address', models.CharField(default='', max_length=20)),
                ('City', models.CharField(default='', max_length=20)),
                ('State', models.CharField(default='', max_length=20)),
                ('Number', models.IntegerField(default=0)),
                ('Profile', models.ImageField(default='', upload_to='home')),
            ],
        ),
    ]
