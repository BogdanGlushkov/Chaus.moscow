# Generated by Django 4.2.1 on 2023-06-15 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_alter_guestlist_promo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guestlist',
            name='promo',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Промокод'),
        ),
    ]
