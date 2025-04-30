import random

def generate_addition_easy():
    first = random.randrange(3, 50)
    second = random.randrange(3, 50)
    return [first, second, first + second]

def generate_subtraction_easy():
    first = random.randrange(3, 50)
    second = random.randrange(3, 50)
    return [first, second, first - second]

def generate_multiplication_easy():
    first = random.randrange(1, 12)
    second = random.randrange(1, 12)
    return [first, second, first * second]



