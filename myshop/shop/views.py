from django.http import Http404
from django.shortcuts import render, redirect
from .models import Category, Product
from cart.forms import CartAddProductForm


def home(request):
    return redirect("product_list")


def product_list(request):
    return get_all_categories(request)


def get_all_categories(request):
    return render(request, "product/list.html", {
        "categories": Category.objects.all(),
        "products": Product.objects.filter(available=True),
    })


def get_category(request, category_slug):
    try:
        category = Category.objects.get(slug=category_slug)
        products = Product.objects.filter(category=category)

        return render(request, "product/list.html", {
            "categories": Category.objects.all(),
            "category": category,
            "products": products,
        })

    except Category.DoesNotExist or Product.DoesNotExist:
        raise Http404


def get_product(request, category_slug, product_slug, product_id):
    try:
        category = Category.objects.get(slug=category_slug)
        product = Product.objects.get(slug=product_slug, available=True, id=product_id)

        cart_product_form = CartAddProductForm()

        return render(request, "product/detail.html", {
            "category": category,
            "product": product,
            "cart_product_form": cart_product_form,
        })
    
    except Category.DoesNotExist or Product.DoesNotExist:
        raise Http404
    
