# Generated by Django 2.2.6 on 2019-12-11 04:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webPage', '0006_choice_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=datetime.date.today, verbose_name='date published'),
        ),
    ]
