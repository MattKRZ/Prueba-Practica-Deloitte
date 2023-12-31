# Generated by Django 4.2.7 on 2023-11-08 03:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_categorias_options_alter_productos_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorias',
            name='category',
            field=models.CharField(max_length=30, verbose_name='Categoria'),
        ),
        migrations.AlterField(
            model_name='productos',
            name='category_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category_id', to='core.categorias', verbose_name='Categoria'),
        ),
        migrations.AlterField(
            model_name='productos',
            name='image_url',
            field=models.CharField(max_length=100, verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='productos',
            name='price',
            field=models.FloatField(verbose_name='Precio'),
        ),
        migrations.AlterField(
            model_name='productos',
            name='product_name',
            field=models.CharField(max_length=50, verbose_name='Nombre Producto'),
        ),
    ]
