# Generated by Django 2.1.3 on 2018-11-09 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0003_auto_20181109_0555'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='display_artist',
            field=models.CharField(default='ok', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='show',
            name='display_city',
            field=models.CharField(default='ok', max_length=200),
            preserve_default=False,
        ),
    ]
