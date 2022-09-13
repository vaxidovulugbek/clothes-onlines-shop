# Generated by Django 4.1 on 2022-08-16 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountapp', '0006_alter_customuser_managers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='city',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='phoneNumber',
            field=models.CharField(blank=True, max_length=13, null=True, unique=True),
        ),
    ]