# Generated by Django 2.0.5 on 2018-05-31 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailverification',
            name='is_delete',
            field=models.BooleanField(default=0, verbose_name='是否已验证'),
        ),
    ]
