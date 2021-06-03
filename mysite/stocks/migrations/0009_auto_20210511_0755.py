# Generated by Django 3.1.5 on 2021-05-11 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0008_auto_20210511_0726'),
    ]

    operations = [
        migrations.AddField(
            model_name='favourite',
            name='close',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='favourite',
            name='fname',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='favourite',
            name='open',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='favourite',
            name='volume',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='favourite',
            name='userid',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
