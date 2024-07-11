# Generated by Django 4.1.3 on 2024-07-11 23:04

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.functions.text


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Art',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', cloudinary.models.CloudinaryField(max_length=255, verbose_name='pic')),
                ('title', models.CharField(blank=True, max_length=250, null=True)),
                ('code', models.CharField(max_length=100)),
                ('style', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=400)),
                ('color', models.BooleanField(default=True)),
                ('frame_type', models.CharField(max_length=100)),
                ('mods', models.BooleanField(default=False)),
                ('date_created', models.DateField(blank=True, null=True)),
                ('film_type', models.CharField(max_length=100)),
                ('malfunction', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ArtTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Fan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddConstraint(
            model_name='tag',
            constraint=models.UniqueConstraint(django.db.models.functions.text.Lower('category'), name='unique_lower_category'),
        ),
        migrations.AddField(
            model_name='arttag',
            name='art',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='thearchiveapi.art'),
        ),
        migrations.AddField(
            model_name='arttag',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='thearchiveapi.tag'),
        ),
        migrations.AddField(
            model_name='art',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='art', through='thearchiveapi.ArtTag', to='thearchiveapi.tag'),
        ),
    ]
