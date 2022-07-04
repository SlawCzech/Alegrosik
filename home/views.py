from django.shortcuts import render

def home_view(request):
    name = 'Alegrosik. Strona startowa'
    hello = 'Witaj! Co możemy dla Ciebie zrobić?'
    return render(request, 'home/home.html', {"name": name, "hello": hello})

