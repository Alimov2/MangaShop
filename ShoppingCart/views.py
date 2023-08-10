from django.shortcuts import redirect, render
from ShoppingCart.shopping_cart import Shopping_Cart_Class
from Store.models import Manga
from django.contrib import messages
# from .models import Product



# Create your views here.
def add_product_cart_store(request, id):
    cart = Shopping_Cart_Class(request)
    product = Manga.objects.get(id=id)

    cart.add_product(product=product)

    messages.success(request, "Добавлено успешно!")

    return redirect("my_manga")


def add_product_cart_page(request, id):
    cart = Shopping_Cart_Class(request)

    product = Manga.objects.get(id=id)

    cart.add_product(product=product)

    return render(request, "my_cart.html")


def del_product_cart(request, id):
    cart = Shopping_Cart_Class(request)
    del_prod = Manga.objects.get(id=id)
    cart.delete_product(del_prod)
    return render(request, "my_cart.html")


def discount_product_cart(request, id):
    cart = Shopping_Cart_Class(request)
    disc_prod = Manga.objects.get(id=id)
    cart.discount_product(disc_prod)

    return render(request, "my_cart.html")


def show_cart(request):
    cart = Shopping_Cart_Class(request)

    return render(request, "my_cart.html")


def clean_cart(request):
    cart = Shopping_Cart_Class(request)
    cart.clean_shopping_cart()

    return render(request, "my_cart.html")

def make_purchase(request):
    if request.method == 'POST':
        cart = Shopping_Cart_Class(request)
        cart.clean_shopping_cart()
        return redirect('conifrincart') 
    return render(request, 'conifrincart.html')
