# Generated by Django 3.0.4 on 2020-04-12 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watcher', '0010_auto_20200412_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='source_id',
            field=models.CharField(help_text='Repository owner/name of Github, or package name if PyPi', max_length=200, verbose_name='source id'),
        ),
    ]
