# Generated by Django 3.0.8 on 2020-08-26 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20200824_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(max_length=250, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='order',
            name='city',
            field=models.CharField(max_length=100, verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='order',
            name='first_name',
            field=models.CharField(max_length=50, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='order',
            name='last_name',
            field=models.CharField(max_length=50, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='order',
            name='postal_code',
            field=models.CharField(max_length=20, verbose_name='Индекс'),
        ),
    ]
