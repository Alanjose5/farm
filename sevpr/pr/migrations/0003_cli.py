# Generated by Django 4.1.5 on 2023-01-26 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pr', '0002_farm_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='cli',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='img')),
                ('spe', models.TextField()),
                ('name', models.CharField(max_length=400)),
            ],
        ),
    ]
