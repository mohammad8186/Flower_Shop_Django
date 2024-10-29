from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm
from django.contrib.auth.decorators import login_required


@login_required
def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})


@login_required
def seller_product_list(request):
    if not request.user.is_seller:
        return redirect('product_list')

    my_products = Product.objects.filter(seller=request.user)
    return render(request, 'products/product_list.html', {'products': my_products, 'seller_products': True})


@login_required
def add_product(request):
    if not request.user.is_seller:
        return redirect('product_list')

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('my_product_list')
    else:
        form = ProductForm()
    return render(request, 'products/add_product.html', {'form': form})


@login_required
def edit_product(request, product_id):
    if not request.user.is_seller:
        return redirect('product_list')

    try:
        product_to_edit = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return redirect('my_products')

    if request.method == 'POST':
        form = ProductForm(data=request.POST, files=request.FILES, instance=product_to_edit)
        if form.is_valid():
            form.save()
            return redirect('my_product_list')
    else:
        form = ProductForm(instance=product_to_edit)
    return render(request, 'products/edit_product.html', {'form': form})
