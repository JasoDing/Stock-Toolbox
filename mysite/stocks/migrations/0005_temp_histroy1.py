# Generated by Django 3.1.5 on 2021-05-08 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0004_auto_20210402_2037'),
    ]

    operations = [
        migrations.CreateModel(
            name='Temp_histroy1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('close', models.FloatField(null=True)),
                ('high', models.FloatField(null=True)),
                ('low', models.FloatField(null=True)),
                ('open', models.FloatField(null=True)),
                ('volume', models.IntegerField(null=True)),
            ],
        ),
    ]
