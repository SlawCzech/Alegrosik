from django.shortcuts import render

def kontakt_view(request):
    kontakt = 'Skontaktuj się z nami!'
    return render(request, 'kontakt/kontakt.html', {"name": kontakt})