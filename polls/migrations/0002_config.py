# Generated by Django 4.2.4 on 2023-08-22 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Config',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('configname', models.CharField(max_length=100)),
                ('test1', models.BooleanField(default=0)),
                ('test2', models.BooleanField(default=0)),
                ('test3', models.BooleanField(default=0)),
            ],
        ),
    ]
