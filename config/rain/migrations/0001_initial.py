# Generated by Django 4.2.7 on 2023-11-24 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('city', '0004_remove_subregion_maxlat_remove_subregion_maxlng_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('regionName', models.CharField(max_length=100)),
                ('sum', models.FloatField(default=0)),
                ('FirstAdded', models.FloatField(default=0)),
                ('AddedCount', models.IntegerField(default=0)),
                ('subRegion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='city.city')),
            ],
            options={
                'db_table': 'rain',
            },
        ),
    ]