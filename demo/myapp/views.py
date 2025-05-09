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
    questions = []
    all = Problem.objects.all()
    
    for _ in range(200):
        qidx = random.randrange(0, len(all))
        while qidx in visit:
            qidx = random.randrange(0, len(all))
        visit.add(qidx)
        q = all[qidx]
        answers = [
        {"text": q.answer, "is_correct": True},
        {"text": q.wa1, "is_correct": False},
        {"text": q.wa2, "is_correct": False},
        {"text": q.wa3, "is_correct": False}
        ]
        
        random.shuffle(answers)
        
        questions.append({
            "id": len(questions) + 1,
            "question": q.question,
            "answers": answers
        })
    
    context = {
        'questions': questions
    }
    return render(request, "compete.html", context)       
    