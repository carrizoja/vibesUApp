# Generated by Django 4.2.3 on 2023-08-12 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppVibesU', '0004_alter_album_image_alter_artist_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='release_date',
            field=models.CharField(max_length=4),
        ),
    ]
