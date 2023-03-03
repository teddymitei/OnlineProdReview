from django.db import models
#import User module
from django.contrib.auth.models import User 

# Create your models here.
#this is used to model the data and database. to make sure the data is set in a way to not make any changes.
class Category(models.Model):
    #name is a variable name
    #data type is Charfield that means we are going to add characters in the field.
    name = models.CharField(max_length=255,db_index=True)
    #slug helps to type in the browser so as to get in the category. unique means there should be only one slug with certain name
    slug = models.SlugField(max_length=255,unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

#associate category with products. build a link between product and category table. on_delete says what happens when change category data
class Product(models.Model):
    category = models.ForeignKey(Category,related_name='product',on_delete=models.CASCADE)
    #product is added to database, record who actually made that data.Building a connection to User table. Building a foreign key to that table
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,related_name='product_creator')
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, default='admin')
    description = models.TextField(blank=True)
    #not storing that image to the database but rather link to the images. have to set up that link
    image = models.ImageField(upload_to='images/')
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=4,decimal_places=2)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    #utilized when actually build a new product. auto now add is gonna happens once
    created = models.DateTimeField(auto_now_add=True)
    #make update to our products. record updates .
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Products'
        #return all data from this product specify order of data. sort by descending(-)
        ordering = ('-created',)
    #return default string of the title. return piece of data , return title of data
    def __str__(self):
        return self.title
    

