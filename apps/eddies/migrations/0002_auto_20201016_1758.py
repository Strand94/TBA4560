# Generated by Django 3.1.2 on 2020-10-16 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eddies', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='searcharea',
            name='bot_right_lat',
        ),
        migrations.RemoveField(
            model_name='searcharea',
            name='bot_right_lng',
        ),
        migrations.RemoveField(
            model_name='searcharea',
            name='top_left_lat',
        ),
        migrations.RemoveField(
            model_name='searcharea',
            name='top_left_lng',
        ),
        migrations.AddField(
            model_name='searcharea',
            name='nw_lat',
            field=models.DecimalField(blank=True, decimal_places=16, max_digits=22, null=True),
        ),
        migrations.AddField(
            model_name='searcharea',
            name='nw_long',
            field=models.DecimalField(blank=True, decimal_places=16, max_digits=22, null=True),
        ),
        migrations.AddField(
            model_name='searcharea',
            name='se_lat',
            field=models.DecimalField(blank=True, decimal_places=16, max_digits=22, null=True),
        ),
        migrations.AddField(
            model_name='searcharea',
            name='se_lon',
            field=models.DecimalField(blank=True, decimal_places=16, max_digits=22, null=True),
        ),
    ]
