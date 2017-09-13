# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-13 08:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='邮箱')),
                ('phone', models.IntegerField(default=0, verbose_name='手机号')),
                ('password', models.CharField(max_length=255, verbose_name='密码')),
                ('account', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='账户余额')),
            ],
        ),
    ]
