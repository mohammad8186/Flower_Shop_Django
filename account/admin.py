from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account


@admin.register(Account)
class AccountAdmin(UserAdmin):
    account_fieldsets = (
        "اطلاعات کاربر", {"fields": ("is_seller", "is_customer")},
    )

    def get_fieldsets(self, request, obj=None):
        fieldsets = list(super().get_fieldsets(request, obj))
        fieldsets.insert(2, self.account_fieldsets)
        return tuple(fieldsets)
