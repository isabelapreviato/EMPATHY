from django.shortcuts import render

# Create your views here.

def index_cadastro1(request):
    return render(request, 'layout_cadastro1.html', {})

def index_cadastro2(request):
    return render(request, 'layout_cadastro2.html', {})