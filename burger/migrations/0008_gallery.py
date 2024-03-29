# Generated by Django 3.2.1 on 2022-03-03 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('burger', '0007_delete_client'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_name', models.CharField(max_length=200, null=True)),
                ('description', models.TextField(blank=True, max_length=1000, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
            options={
                'verbose_name_plural': 'Gallery',
            },
        ),
    ]
