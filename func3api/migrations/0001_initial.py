# Generated by Django 3.0.6 on 2020-05-06 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cComid', models.CharField(max_length=20)),
                ('cPosition', models.CharField(max_length=20)),
                ('cName', models.CharField(max_length=20)),
                ('cSharemoney', models.CharField(max_length=30)),
            ],
        ),
    ]
