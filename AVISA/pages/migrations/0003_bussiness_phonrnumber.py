# Generated by Django 2.2.20 on 2022-01-28 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20220128_1003'),
    ]

    operations = [
        migrations.AddField(
            model_name='bussiness',
            name='phonrnumber',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
