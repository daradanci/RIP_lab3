# Generated by Django 4.1.1 on 2022-09-18 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('dogid', models.AutoField(db_column='dogId', primary_key=True, serialize=False)),
                ('dogname', models.CharField(db_column='dogName', max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Range',
            fields=[
                ('rangeid', models.AutoField(db_column='rangeId', primary_key=True, serialize=False)),
                ('rangename', models.CharField(db_column='rangeName', max_length=30, unique=True)),
            ],
        ),
    ]