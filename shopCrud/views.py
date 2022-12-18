from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from django.urls import reverse

from .models import *

def index(request):

    my_data = Product.objects.all()
    # one_data = Product.objects.get(pk=1)  # 1 will return the first item change it depending on the data you want
    context = {

        'my_data': my_data,
        # 'one_data': one_data,

    }

    return render(request, 'shopCrud/index.html',context)

def detail(request, item_id):

    one_data = Product.objects.get(pk= item_id)
    context = {

        'one_data': one_data,

    }
    return render(request, 'shopCrud/product.html', context)

def add(request):
  template = loader.get_template('shopCrud/add.html')
  return HttpResponse(template.render({}, request))

def addproduct(request):
  name = request.POST['name']
  price = request.POST['price']
  stock = request.POST['stock']
  image = request.POST['image']

  product = Product(name=name, price=price, stock=stock, image=image)
  product.save()
  return HttpResponseRedirect(reverse('shopCrud:index'))

def delete(request, item_id):
    one_data = Product.objects.get(pk=item_id)
    one_data.delete()

    return HttpResponseRedirect(reverse('shopCrud:index'))