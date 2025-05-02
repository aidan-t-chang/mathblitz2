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
        new = {'question': q, 'answer': question[2]}
        if q not in visit:
            math_problems.append(new)
        
    Problem.objects.bulk_create([
        Problem(**problem) for problem in math_problems
    ])
    
    
def populate_subtraction_easy():
    math_problems = []
    visit = set()
    for _ in range(10000):
        question = generate_subtraction_easy()
        q = str(question[0]) + "-" + str(question[1])
        new = {'question': q, 'answer': question[2]}
        if q not in visit:
            math_problems.append(new)
            
    Problem.objects.using('subtraction').bulk_create([
        Problem(**problem) for problem in math_problems
    ])   

def populate_multiplication_easy():
    math_problems = []
    visit = set()
    for _ in range(10000):
        question = generate_multiplication_easy()
        q = str(question[0]) + "*" + str(question[1])
        new = {'question': q, 'answer': question[2]}
        if q not in visit:
            math_problems.append(new)
            
    Problem.objects.using('multiplication').bulk_create([
        Problem(**problem) for problem in math_problems
    ])    

populate_subtraction_easy()
populate_multiplication_easy()
print('successfully populated!')

        
