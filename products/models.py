from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True) 
    image = models.ImageField(upload_to='media/categories', verbose_name='image', blank=True, null=True)
  
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'categories'

class Products(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    stock = models.BooleanField(default=True)
    image = models.ImageField(upload_to='products', verbose_name='image')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
  
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

