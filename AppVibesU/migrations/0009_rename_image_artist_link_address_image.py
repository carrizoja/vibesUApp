# Generated by Django 4.2.3 on 2023-09-02 18:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppVibesU', '0008_song_mp3_track'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artist',
            old_name='image',
            new_name='link_address_image',
        ),
    ]