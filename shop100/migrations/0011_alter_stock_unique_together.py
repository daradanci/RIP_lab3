# Generated by Django 4.1.1 on 2022-09-18 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop100', '0010_stock_amount_stock_size'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='stock',
            unique_together={('idmodel', 'size')},
        ),
    ]
