# Generated by Django 4.0 on 2022-05-09 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_flighttocity_from_to'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flighttocity',
            name='company',
        ),
        migrations.RemoveField(
            model_name='flighttocity',
            name='from_to',
        ),
        migrations.RemoveField(
            model_name='flighttocity',
            name='start_time',
        ),
        migrations.RemoveField(
            model_name='flighttocity',
            name='wait_time',
        ),
        migrations.AddField(
            model_name='flighttocity',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='flighttocity',
            name='type',
            field=models.CharField(choices=[('Бизнес', 'Бизнес'), ('Эконом', 'Эконом')], default='Эконом', max_length=10),
        ),
        migrations.AddField(
            model_name='hoteltocity',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userevent',
            name='flightToCity',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.flighttocity'),
        ),
        migrations.AddField(
            model_name='userevent',
            name='hotel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.hoteltocity'),
        ),
    ]