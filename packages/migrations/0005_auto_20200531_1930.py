# Generated by Django 3.0.5 on 2020-05-31 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0004_auto_20200531_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='name'),
        ),
    ]
