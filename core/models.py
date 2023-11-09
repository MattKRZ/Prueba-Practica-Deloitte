from django.db import models

# Create your models here.
class Categorias(models.Model):
    id = models.BigAutoField(primary_key=True)
    category = models.CharField(max_length=30, verbose_name='Categoria')

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self) -> str:
        return self.category

class Productos(models.Model):
    id = models.BigAutoField(primary_key=True)
    product_name = models.CharField(max_length=50, verbose_name='Nombre Producto')
    description = models.TextField(max_length=100, verbose_name='Descripcion Producto', null=True)
    image_url = models.CharField(max_length=400, verbose_name='Imagen')
    price = models.FloatField(verbose_name='Precio')
    category_id = models.ForeignKey(Categorias, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Categoria')

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
    
    def __str__(self) -> str:
        return self.product_name