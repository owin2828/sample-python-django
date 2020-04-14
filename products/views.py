from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Product


def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products':products})


def new(request):
    return render(request, 'new.html')


def insert(request):

    new_product = Product(
        name=request.POST.get("name"),
        price=request.POST.get("price"),
        stock=request.POST.get("stock"),
        image_url=request.POST.get("img_url"),
    )
    new_product.save()
    return HttpResponseRedirect('/products')


def delete(request):
    Product.objects.get(id=request.GET.get("id")).delete()
    return HttpResponseRedirect("/products")


def updateform(request):
    product = Product.objects.get(id=request.GET.get("id"))
    return render(request, 'update.html', {"product": product})


def update(request):
    product = Product(
        id=request.POST.get("id"),
        name=request.POST.get("name"),
        price=request.POST.get("price"),
        stock=request.POST.get("stock"),
        image_url=request.POST.get("img_url"),
    )
    product.save()
    return HttpResponseRedirect("/products")


