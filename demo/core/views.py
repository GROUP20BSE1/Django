from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def goToHomePage(request):
    return render(request, "core/index.html")