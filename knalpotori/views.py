from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

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
    
def login(request):
    context = {}
    return render(request, 'login.html', context)