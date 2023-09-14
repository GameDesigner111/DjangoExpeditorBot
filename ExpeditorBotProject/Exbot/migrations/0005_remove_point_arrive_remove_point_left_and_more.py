# Generated by Django 4.2.4 on 2023-09-04 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Exbot', '0004_point_arrive_point_left'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='point',
            name='arrive',
        ),
        migrations.RemoveField(
            model_name='point',
            name='left',
        ),
        migrations.AddField(
            model_name='point',
            name='arrived_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Прибыл'),
        ),
        migrations.AddField(
            model_name='point',
            name='left_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Уехал'),
        ),
    ]