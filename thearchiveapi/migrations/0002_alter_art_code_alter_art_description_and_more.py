# Generated by Django 4.1.3 on 2024-01-17 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thearchiveapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='art',
            name='code',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='art',
            name='description',
            field=models.CharField(max_length=400),
        ),
        migrations.AlterField(
            model_name='art',
            name='film_type',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='art',
            name='frame_type',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='art',
            name='location',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='art',
            name='style',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='art',
            name='title',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
