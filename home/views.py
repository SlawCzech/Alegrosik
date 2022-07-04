from django.shortcuts import render

def home_view(request):
    name = 'Alegrosik. Strona startowa'
    return render(request, 'home/home.html', {"name": name})

