# Generated by Django 2.1.3 on 2018-11-09 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0002_shows'),
    ]

    operations = [
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('start_time', models.DateTimeField()),
                ('description', models.TextField()),
                ('added_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Shows',
        ),
    ]