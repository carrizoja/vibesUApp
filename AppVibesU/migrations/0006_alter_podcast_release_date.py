# Generated by Django 4.2.3 on 2023-08-12 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppVibesU', '0005_alter_album_release_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='podcast',
            name='release_date',
            field=models.CharField(max_length=4),
        ),
    ]