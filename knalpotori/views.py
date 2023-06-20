from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



# Create your views here.

""" def index(request):
    template = loader.get_template('beranda.html')
    context = {
        'title' : 'Django | Pemrograman 1',
        'img_product' : 'https://cdn.juraganwp.com/aripitstop/wp-content/uploads/2018/08/knalpot-indolingga-2.jpg',
        'product_name' : 'Knalpot Original',
        'product_list' : [1,2,3,4,5],
    }
    return HttpResponse(template.render(context,request)) 
    
def login(request):
    template = loader.get_template('login.html')
    context = {}
    return HttpResponse(template.render(context,request))
    
"""

# Code diatas dapat disederhanakan menjadi seperti dibawah ini 

def index (request):
    context = {
    'title' : 'Django | Pemrograman 1',
    'img_product' : 'https://cdn.juraganwp.com/aripitstop/wp-content/uploads/2018/08/knalpot-indolingga-2.jpg',
    'product_name' : 'Knalpot Original',
    'product_list' : [1,2,3,4,5],
    }
    return render(request, 'beranda.html', context)

def mobil(request):
	template = loader.get_template('product.html')
	context = {
		'title' : 'knalpotori.id | original exhaust',
		'img_product' : 'img/produk.jpg',
		'product_name' : 'Kategori Knalpot Mobil',
		'product_list' : [1,2,3,4,5,6,7],
	}
	return HttpResponse(template.render(context,request))

def motor(request):
	template = loader.get_template('product.html')
	context = {
		'title' : 'knalpotori.id | original exhaust',
		'img_product' : 'img/produk.jpg',
		'product_name' : 'Knalpot Motor Racing',
		'product_list' : [11,12,13,14,15,16,17,18,19,20],
	}
	return HttpResponse(template.render(context,request))

def aksesoris(request):
	template = loader.get_template('product.html')
	context = {
		'title' : 'knalpotori.id | original exhaust',
		'img_product' : 'img/produk.jpg',
		'product_name' : 'Aksesoris Otomotif',
		'product_list' : [11,12,13],
	}
	return HttpResponse(template.render(context,request))

def detail(request):
	template = loader.get_template('detail.html')
	context = {
		'title' : 'knalpotori.id | original exhaust',
		'img_product' : 'img/produk.jpg',
		'product_name' : 'Detail Produk',
		'product_list' : [1,2,3,4,5],
	}
	return HttpResponse(template.render(context,request))

def registrasi(request):
	template = loader.get_template('product.html')
	context = {
		'title' : 'knalpotori.id | original exhaust',
		'img_product' : 'https://cdn.juraganwp.com/aripitstop/wp-content/uploads/2018/08/knalpot-indolingga-2.jpg',
		'product_name' : 'Knalpot Mobil',
		'product_list' : [1,2,3,4,5],
	}
	return HttpResponse(template.render(context,request))

def login(request):
	template = loader.get_template('login.html')
	context = {}
	return HttpResponse(template.render(context,request))

def cart(request):
	template = loader.get_template('product.html')
	context = {
		'title' : 'knalpotori.id | original exhaust',
		'img_product' : 'https://cdn.juraganwp.com/aripitstop/wp-content/uploads/2018/08/knalpot-indolingga-2.jpg',
		'product_name' : 'Keranjang Belanja',
		'product_list' : [1,2,3,4,5],
	}
	return HttpResponse(template.render(context,request))