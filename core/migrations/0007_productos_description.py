# Generated by Django 4.2.7 on 2023-11-08 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_delete_customuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='productos',
            name='description',
            field=models.TextField(max_length=100, null=True, verbose_name='Descripcion Producto'),
        ),
    ]