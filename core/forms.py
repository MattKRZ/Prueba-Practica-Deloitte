from django.forms import ModelForm
from .models import Productos

class ProductosForm(ModelForm):
    class Meta:
        model = Productos
        fields = ['product_name','description', 'image_url', 'price', 'category_id']