# Generated by Django 4.2.7 on 2023-11-08 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_productos_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='image_url',
            field=models.CharField(max_length=200, verbose_name='Imagen'),
        ),
    ]
