from django.shortcuts import render, HttpResponse
# Create your views here.
def home(request):
    return render(request, "home.html")

def profile(request):
    return render(request, "profile.html")

def compete(request):
    return render(request, "compete.html")