# Generated by Django 4.2.7 on 2023-11-24 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('city', '0002_subregion'),
    ]

    operations = [
        migrations.AddField(
            model_name='subregion',
            name='detail',
            field=models.CharField(max_length=100, null=True),
        ),
    ]