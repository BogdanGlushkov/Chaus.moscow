# Generated by Django 4.2.1 on 2023-07-02 02:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_alter_guestlist_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guestlist',
            name='event',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.event'),
        ),
    ]
