# Generated by Django 3.2.1 on 2022-03-02 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('burger', '0002_auto_20220302_1356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='price',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
