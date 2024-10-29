from django.db import models
from django.contrib.auth import get_user_model


class Product(models.Model):
    seller = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='فروشنده')
    name = models.CharField(max_length=100, verbose_name='نام محصول')
    description = models.TextField(verbose_name='توضیحات')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='قیمت')
    image = models.ImageField(upload_to='product_images/', blank=True, null=True, verbose_name='تصویر محصول')

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

    def __str__(self):
        return self.name
