# Generated by Django 3.1.6 on 2021-02-18 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='locale',
            field=models.CharField(blank=True, default='', max_length=128, null=True, verbose_name='ロケール'),
        ),
    ]
