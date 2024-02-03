# Generated by Django 5.0.1 on 2024-02-03 07:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cadastral_number', models.CharField(max_length=15, verbose_name='кадастровый номер')),
                ('latitude', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='широта')),
                ('longitude', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='долгота')),
            ],
            options={
                'verbose_name': 'запрос',
                'verbose_name_plural': 'запросы',
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.BooleanField(verbose_name='значение ответа')),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer', to='main.request', verbose_name='запрос')),
            ],
            options={
                'verbose_name': 'ответ',
                'verbose_name_plural': 'ответы',
            },
        ),
    ]
