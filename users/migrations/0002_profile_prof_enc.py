# Generated by Django 3.0.6 on 2020-05-18 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='prof_enc',
            field=models.BinaryField(default=b'hello world'),
        ),
    ]