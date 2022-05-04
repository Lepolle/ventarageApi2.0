from django.contrib.auth.models import AbstractUser
from django.db import models
from django.template.defaultfilters import slugify


def path_to_avatar(instance, filename):
    return f'avatars/{instance.id}/{filename}'


def path_to_products(instance, filename):
    return f'products/{instance.id}/{filename}'


def path_to_categories(instance, filename):
    return f'categories/{instance.id}/{filename}'


class CustomUser(AbstractUser):
    email = models.EmailField(
        max_length=150, unique=True)
    avatar = models.ImageField(
        upload_to=path_to_avatar, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'password']


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    img = models.ImageField(upload_to=path_to_categories, blank=True, null=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.DO_NOTHING)
    slug = models.SlugField(max_length=200, db_index=True)
    name = models.CharField(max_length=250, blank=False, null=False)
    img = models.ImageField(upload_to=path_to_products, default=f'products/noimage.png')
    descripcion = models.TextField(max_length=1000, blank=True, null=False)
    precio = models.DecimalField(decimal_places=2, max_digits=1000, blank=False, null=False)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

