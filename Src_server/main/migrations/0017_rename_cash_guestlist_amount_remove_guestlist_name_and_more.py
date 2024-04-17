# Generated by Django 4.2.1 on 2023-07-01 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_selectedphoto_delete_selectorphoto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='guestlist',
            old_name='cash',
            new_name='amount',
        ),
        migrations.RemoveField(
            model_name='guestlist',
            name='Name',
        ),
        migrations.AddField(
            model_name='guestlist',
            name='status',
            field=models.CharField(default='New', max_length=30, verbose_name='Статус'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='guestlist',
            name='email',
            field=models.CharField(max_length=255, verbose_name='E-mail*'),
        ),
        migrations.AlterField(
            model_name='guestlist',
            name='phone',
            field=models.CharField(max_length=20, verbose_name='Телефон*'),
        ),
        migrations.DeleteModel(
            name='SelectedPhoto',
        ),
        migrations.AddField(
            model_name='guestlist',
            name='name',
            field=models.CharField(default='Noname', max_length=255, verbose_name='ФИО*'),
            preserve_default=False,
        ),
    ]