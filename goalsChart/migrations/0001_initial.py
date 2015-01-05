# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name_goal', models.CharField(max_length=50)),
                ('cost_goal', models.DecimalField(verbose_name=b'Goal Cost', max_digits=10, decimal_places=2)),
                ('date_goal', models.DateTimeField(verbose_name=b'Goal Date')),
                ('start_goal', models.DateTimeField(verbose_name=b'Goal Start')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_name', models.CharField(max_length=50)),
                ('profile_create_date', models.DateTimeField(verbose_name=b'User Since')),
                ('min_balance', models.DecimalField(verbose_name=b'Minimum Balance', max_digits=10, decimal_places=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='goal',
            name='user',
            field=models.ForeignKey(to='goalsChart.User'),
            preserve_default=True,
        ),
    ]
