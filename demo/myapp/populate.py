from myapp.models import Problem 
from myapp.questions import generate_addition_easy, generate_multiplication_easy, generate_subtraction_easy
import os
import django


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demo.settings')
django.setup()

def populate_addition_easy():
    math_problems = []
    visit = set()
    for _ in range(10000):
        question = generate_addition_easy()
        q = str(question[0]) + "+" + str(question[1])
        new = {'question': q, 'answer': question[2], 'wa1': question[3], 'wa2': question[4], 'wa3': question[5]}
        if q not in visit:
            math_problems.append(new)
        
    Problem.objects.bulk_create([
        Problem(**problem) for problem in math_problems
    ])
    Problem.objects.all().delete()
    
    
def populate_subtraction_easy():
    math_problems = []
    visit = set()
    for _ in range(10000):
        question = generate_subtraction_easy()
        q = str(question[0]) + "-" + str(question[1])
        new = {'question': q, 'answer': question[2], 'wa1': question[3], 'wa2': question[4], 'wa3': question[5]}
        if q not in visit:
            math_problems.append(new)
            
    Problem.objects.using('subtraction').bulk_create([
        Problem(**problem) for problem in math_problems
    ])   
    Problem.objects.all().delete()

def populate_multiplication_easy():
    math_problems = []
    visit = set()
    for _ in range(10000):
        question = generate_multiplication_easy()
        q = str(question[0]) + "*" + str(question[1])
        new = {'question': q, 'answer': question[2], 'wa1': question[3], 'wa2': question[4], 'wa3': question[5]}
        if q not in visit:
            math_problems.append(new)
            
    Problem.objects.using('multiplication').bulk_create([
        Problem(**problem) for problem in math_problems
    ])    
    Problem.objects.all().delete()

populate_addition_easy()
populate_subtraction_easy()
populate_multiplication_easy()
print('successfully populated!')

        
