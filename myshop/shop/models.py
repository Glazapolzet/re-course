from django.db import models
from parler.models import TranslatableModel, TranslatedFields


class Category(TranslatableModel):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    # translations = TranslatedFields(
    #     name=models.CharField(max_length=200, db_index=True),
    #     slug=models.SlugField(max_length=200, db_index=True, unique=True),
    # )

    def __str__(self):
        # return self.name
        return "Category"
    
    class Meta:
        ordering = ('name',)
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def get_absolute_url(self):
        return f"/shop/{self.slug}"


class Product(TranslatableModel):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    description = models.TextField(blank=True)

    # translations = TranslatedFields(
    #     name=models.CharField(max_length=200, db_index=True),
    #     slug=models.SlugField(max_length=200, db_index=True),
    #     description=models.TextField(blank=True)
    # )
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/%Y/%m/%d', null=True, blank=True, verbose_name='Изображение')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        # return self.name
        return "Product"
    
    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def get_absolute_url(self):
        return f"/shop/{self.category.slug}/{self.slug}/{self.id}"

