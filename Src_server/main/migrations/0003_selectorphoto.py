# Generated by Django 4.2.1 on 2023-06-14 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_event_link1_remove_event_link2_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SelectorPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Блок с фотографиями', max_length=250, verbose_name='Ссылка на фото')),
                ('event', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.event')),
            ],
        ),
    ]
