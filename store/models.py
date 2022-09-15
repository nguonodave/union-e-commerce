from asyncio.windows_events import NULL
from distutils.command.upload import upload
from email.mime import image
from operator import mod
from django.db import models
from category.models import Category
from django.core.validators import MinValueValidator
from django.urls import reverse

class Product(models.Model):
    product_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(max_length=500, blank=True)
    price = models.IntegerField(validators=[MinValueValidator(1)])
    images = models.ImageField(upload_to='photos/products')
    stock = models.IntegerField(validators=[MinValueValidator(0)])
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.stock >= 1:
            self.is_available = True
            super(Product, self).save(*args, **kwargs)
        elif self.stock == 0:
            self.is_available = False
            super(Product, self).save(*args, **kwargs)
    
    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])
        # the above, self is the product, category is the product's category above, the first slug is the slug of the category, NOT the product and the second slug is the product's slug
        
    def __str__(self):
        return self.product_name
    



