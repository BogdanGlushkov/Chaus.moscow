# Generated by Django 4.2.1 on 2023-06-14 15:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='link1',
        ),
        migrations.RemoveField(
            model_name='event',
            name='link2',
        ),
        migrations.RemoveField(
            model_name='event',
            name='link3',
        ),
        migrations.RemoveField(
            model_name='event',
            name='link4',
        ),
        migrations.RemoveField(
            model_name='event',
            name='link5',
        ),
        migrations.RemoveField(
            model_name='event',
            name='link6',
        ),
        migrations.RemoveField(
            model_name='event',
            name='link7',
        ),
        migrations.RemoveField(
            model_name='event',
            name='link8',
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(default='https://sun9-32.userapi.com/impg/zrz3r538SYbayNk3qmPyFzgDfNELnXtSjF4Epw/nnLVZniRHZ4.jpg?size=740x740&quality=95&sign=3eaa2b0afe565c75dcd40bd86c6dbb47&type=album', max_length=250, verbose_name='Ссылка на фото')),
                ('event', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.event')),
            ],
            options={
                'verbose_name': 'Фото',
                'verbose_name_plural': 'Фотографии',
            },
        ),
        migrations.CreateModel(
            name='EventLinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='#', max_length=250, verbose_name='Подробнее')),
                ('event', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.event')),
            ],
            options={
                'verbose_name': 'Ссылка',
                'verbose_name_plural': 'Ссылки',
            },
        ),
    ]
