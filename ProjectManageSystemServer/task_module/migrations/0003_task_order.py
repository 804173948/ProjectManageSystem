# Generated by Django 2.2.6 on 2019-10-18 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_module', '0002_auto_20191016_0245'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='order',
            field=models.PositiveSmallIntegerField(null=True),
        ),
    ]
