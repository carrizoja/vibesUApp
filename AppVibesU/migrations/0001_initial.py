# Generated by Django 4.2.3 on 2023-08-09 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('artist', models.CharField(max_length=50)),
                ('genre', models.CharField(max_length=50)),
                ('release_date', models.DateField()),
                ('amount_of_songs', models.IntegerField()),
                ('album_duration', models.CharField(max_length=10)),
                ('is_favorite', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('genre', models.CharField(max_length=50)),
                ('listeners', models.IntegerField()),
                ('is_favorite', models.BooleanField(default=False)),
                ('is_verified', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Podcast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('host', models.CharField(max_length=50)),
                ('genre', models.CharField(max_length=50)),
                ('release_date', models.DateField()),
                ('amount_of_episodes', models.IntegerField()),
                ('podcast_duration', models.CharField(max_length=10)),
                ('is_favorite', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('artist', models.CharField(max_length=50)),
                ('album', models.CharField(max_length=50)),
                ('length', models.CharField(max_length=10)),
                ('plays', models.IntegerField()),
                ('is_favorite', models.BooleanField(default=False)),
            ],
        ),
    ]
