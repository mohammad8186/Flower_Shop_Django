from django.contrib.auth.models import AbstractUser
from django.db import models


class Account(AbstractUser):
    is_seller = models.BooleanField(default=False, verbose_name='آیا فروشنده است؟')
    is_customer = models.BooleanField(default=False, verbose_name='آیا خریدار است؟')

    class Meta(AbstractUser.Meta):
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'
