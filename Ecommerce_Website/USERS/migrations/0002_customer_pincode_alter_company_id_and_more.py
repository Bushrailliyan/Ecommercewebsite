# Generated by Django 4.2.16 on 2024-11-07 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('USERS', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='pincode',
            field=models.CharField(default=None, max_length=15),
        ),
        migrations.AlterField(
            model_name='company',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='company',
            name='phone',
            field=models.CharField(blank=True, default=None, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(blank=True, default=None, max_length=15, null=True),
        ),
    ]
