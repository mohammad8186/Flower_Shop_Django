from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

from account.models import Account


class RegisterForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ["username", "is_seller", "is_customer", "password1", "password2"]
        labels = {"is_customer": "ثبت نام به عنوان خریدار", "is_seller": "ثبت نام به عنوان فروشنده"}


class LoginForm(AuthenticationForm):
    class Meta:
        model = Account
        fields = ["username", "password"]
