# Generated by Django 4.2.1 on 2023-06-15 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_alter_guestlist_promo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photo',
            options={'verbose_name': 'Событие в блоке фотографии', 'verbose_name_plural': 'События в блоке фотографии'},
        ),
        migrations.AddField(
            model_name='photo',
            name='count',
            field=models.PositiveSmallIntegerField(default=5, verbose_name='Количество фото'),
        ),
        migrations.AddField(
            model_name='photo',
            name='link_Album',
            field=models.CharField(default='#', max_length=250, verbose_name='Ссылка на альбом'),
        ),
        migrations.AlterField(
            model_name='guestlist',
            name='cash',
            field=models.IntegerField(verbose_name='Сумма'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='link',
            field=models.CharField(default='#', max_length=250, verbose_name='Ссылка на главное фото'),
        ),
    ]
