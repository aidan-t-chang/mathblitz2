from django.shortcuts import render, HttpResponse
from .models import Problem
import random
# Create your views here.
def home(request):
    return render(request, "home.html")

def profile(request):
    return render(request, "profile.html")

def compete(request):
    visit = set()
    c = []
    for i in range(10):
        j = random.randrange(0, 1000)
        visit.add(j)
        c.append(Problem.objects.all()[j])
    
    context = {'items': c}
    return render(request, "compete.html", context)