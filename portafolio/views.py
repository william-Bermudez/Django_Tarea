from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def william(request):
    return render(request, 'william.html')

def victor(request):
    return render(request, 'victor.html')

def emely(request):
    return render(request, 'emely.html')

def nelson(request):
    return render(request, 'nelson.html')

def franklin(request):
    return render(request, 'franklin.html')
