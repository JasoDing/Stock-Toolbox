# Generated by Django 3.1.5 on 2021-05-09 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0005_temp_histroy1'),
    ]

    operations = [
        migrations.AddField(
            model_name='temp_histroy1',
            name='ticker',
            field=models.CharField(max_length=10, null=True),
        ),
    ]