# Generated by Django 3.0.3 on 2020-11-09 12:25

from django.db import migrations
import django.utils.timezone
import picklefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Mycustomer', '0028_auto_20200409_1646'),
    ]

    operations = [
        migrations.AddField(
            model_name='eucationloan',
            name='model',
            field=picklefield.fields.PickledObjectField(default=django.utils.timezone.now, editable=False),
            preserve_default=False,
        ),
    ]