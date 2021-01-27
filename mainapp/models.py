from django.db import models


# Create your models here.
class ProductCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название товара')
    image = models.ImageField(upload_to='products_images', blank=True, verbose_name='Фото товара')
    description = models.TextField(blank=True, null=True)
    short_description = models.CharField(max_length=50, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits= 8,default=0,)
    quantity = models.IntegerField(default=0)
    category_id = models.ForeignKey(ProductCategory, on_delete=models.CASCADE,default=1)

    def __str__(self):
        return self.name
