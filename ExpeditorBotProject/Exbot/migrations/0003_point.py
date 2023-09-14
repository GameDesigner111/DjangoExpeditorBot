# Generated by Django 4.2.4 on 2023-09-02 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Exbot', '0002_user_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=50, verbose_name='Адрес точки')),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='points', to='Exbot.user')),
            ],
        ),
    ]