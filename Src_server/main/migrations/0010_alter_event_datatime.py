# Generated by Django 4.2.1 on 2023-06-14 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_remove_event_day_remove_event_month_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='dataTime',
            field=models.DateTimeField(verbose_name='Дата и время начала'),
        ),
    ]
