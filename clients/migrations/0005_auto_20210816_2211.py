# Generated by Django 3.1.4 on 2021-08-16 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0004_auto_20210816_1802'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='client',
        ),
        migrations.AlterField(
            model_name='client',
            name='phone_number',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='client',
            name='site_url',
            field=models.URLField(),
        ),
    ]
