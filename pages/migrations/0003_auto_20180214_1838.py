# Generated by Django 2.0.2 on 2018-02-14 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20180209_1850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='date_of_birth',
            field=models.DateField(verbose_name='Date of Birth'),
        ),
    ]
