# Generated by Django 3.0.4 on 2020-04-16 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watcher', '0018_auto_20200416_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='message',
            field=models.TextField(blank=True, verbose_name='message'),
        ),
    ]