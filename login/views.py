from django.shortcuts import render

# Create your views here.

def index_login(request):
    return render(request, 'layout_login.html', {})