# Generated by Django 4.1.1 on 2022-09-18 14:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop100', '0006_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='idmodel',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.DO_NOTHING, to='shop100.models', verbose_name='idModel'),
        ),
    ]
