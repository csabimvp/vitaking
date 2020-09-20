from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ("name",)
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("shop:product_list_by_category", args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(
        Category, related_name="products", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to="product/%Y/%m/%d", blank=True)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    available = models.BooleanField(default=True)
    on_sale = models.BooleanField(default=False)
    on_sale_price = models.IntegerField(blank=True)
    weight = models.IntegerField()
    units = models.IntegerField()
    daily_dose = models.IntegerField()
    ogyei_number = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("name",)
        index_together = (("id", "slug"),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("shop:product_detail", args=[self.id, self.slug])


class ProductDescription(models.Model):
    product = models.ForeignKey(
        Product, related_name="product_description", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=250, default=False)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product, related_name="product_image", on_delete=models.CASCADE
    )
    image = models.ImageField()
