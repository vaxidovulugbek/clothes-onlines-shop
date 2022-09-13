import json
import uuid

from django.db import models


# models: Category, Product, Size, Color => read project_str.txt for more information
# abstract model: BaseModel => read project_str.txt for more information


# Create your models here.
class BaseModel(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    name = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-created_on', ]


class Category(BaseModel):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

    @property
    def getAmountOfProduct(self):
        return self.products.all().count()

    @property
    def getProductsByCategory(self):
        products = self.products.all()
        return json.dumps(products)


class Size(BaseModel):
    SIZE_CHOOSE = [
        ('x', 'X'),
        ('xl', 'XL'),
    ]
    sz = models.CharField(choices=SIZE_CHOOSE, max_length=4)

    def __str__(self):
        return str(self.sz)


class Color(BaseModel):
    def __str__(self):
        return str(self.name)


class Product(BaseModel):
    STATUS_PRODUCT = [
        ('arrived', 'Arrived'),
        ('trandy', 'Trandy')
    ]
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    color = models.ManyToManyField(Color, related_name='products')
    size = models.ManyToManyField(Size, related_name='products')
    description = models.TextField()
    image = models.FileField(upload_to='products')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=200, choices=STATUS_PRODUCT, null=True, blank=True)

    def __str__(self):
        return self.name
