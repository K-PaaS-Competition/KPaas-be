# Generated by Django 4.2.7 on 2023-11-20 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subway', '0002_rename_latitude_subway_lat_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subway',
            name='line',
            field=models.CharField(max_length=100),
        ),
    ]
