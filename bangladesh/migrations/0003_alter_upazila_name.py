# Generated by Django 4.1.1 on 2023-10-20 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bangladesh', '0002_remove_upazila_lat_remove_upazila_long_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upazila',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
