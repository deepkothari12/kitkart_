from django.db import models
from category.models import Category 
from django.urls import reverse

# Create your models here.
class product(models.Model):
    product_name = models.CharField(max_length=200, unique=True)
    product_slug = models.SlugField(max_length=200, unique=True , help_text="a label for URL config" , auto_created=True) ##nothing but url
    # print(product_slug)
    priduct_description = models.TextField(max_length=500, blank=True)
    product_price = models.IntegerField()                  
    product_image = models.ImageField(upload_to='photos/products')
    product_stock = models.IntegerField()
    is_available  = models.BooleanField(default=True)
    category_fk   = models.ForeignKey(Category, on_delete=models.CASCADE) #Foreign key to link with category table
    # on_delete=models.CASCADE --> tells the database that when an instance of the parent model 
    # (the one being referenced) is deleted, all related child model instances that reference it should also be automatically 
    
    product_created_date = models.DateTimeField(auto_now_add=True)
    product_updated_date = models.DateTimeField(auto_now=True)


    def get_url(self):
        # print("--->>>", self.Category.category_slug , self.product_slug)
        return reverse('product_details' , args=[self.category_fk.category_slug , self.product_slug])  ##to make dynamic url for each product

    def __str__(self):
        return self.product_name