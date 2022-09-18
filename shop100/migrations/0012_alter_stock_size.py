# Generated by Django 4.1.1 on 2022-09-18 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop100', '0011_alter_stock_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='size',
            field=models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'Extra large'), ('XXL', 'Extra extra large')], default='M', max_length=4),
        ),
    ]