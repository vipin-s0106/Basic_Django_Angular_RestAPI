# Generated by Django 3.0.4 on 2020-04-11 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='desc',
            field=models.CharField(default='na', max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movie',
            name='year',
            field=models.IntegerField(default=2000, max_length=4),
            preserve_default=False,
        ),
    ]
