# Generated by Django 4.2.4 on 2023-09-03 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Exbot', '0003_point'),
    ]

    operations = [
        migrations.AddField(
            model_name='point',
            name='arrive',
            field=models.CharField(choices=[('YES', 'ДА'), ('NO', 'НЕТ')], default='NO', max_length=4, verbose_name='Приехал'),
        ),
        migrations.AddField(
            model_name='point',
            name='left',
            field=models.CharField(choices=[('YES', 'ДА'), ('NO', 'НЕТ')], default='NO', max_length=4, verbose_name='Уехал'),
        ),
    ]
