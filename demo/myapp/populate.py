from models import Problem 
from questions import generate_addition_easy, generate_multiplication_easy, generate_subtraction_easy
import os
import django


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demo.settings')
django.setup()

def populate_addition_easy():
    math_problems = []
    for _ in range(10):
        question = generate_addition_easy()
        q = str(question[0]) + "+" + str(question[1])
        new = {'question': q, 'answer': question[2]}
        math_problems.append(new)
        
    Problem.objects.bulk_create([
        Problem(**problem) for problem in math_problems
    ])


populate_addition_easy()


        
