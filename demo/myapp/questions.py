import random

def generate_addition_easy():
    first = random.randrange(3, 50)
    second = random.randrange(3, 50)
    notin = set()
    notin.add(first+second)
    wa1 = random.randrange(0, 70)
    while wa1 in notin:
        wa1 = random.randrange(0, 73)
    notin.add(wa1)
    wa2 = random.randrange(0, 70)
    while wa2 in notin: 
        wa2 = random.randrange(0, 70)
    notin.add(wa2) 
    wa3 = random.randrange(0, 70)
    while wa3 in notin: 
        wa3 = random.randrange(0, 70)
    return [first, second, first + second, wa1, wa2, wa3]

def generate_subtraction_easy():
    first = random.randrange(3, 50)
    second = random.randrange(3, 50)
    notin = set()
    notin.add(first-second)
    wa1 = random.randrange(-48, 48)
    while wa1 in notin:
        wa1 = random.randrange(-48, 48)
    notin.add(wa1)
    wa2 = random.randrange(-48, 48)
    while wa2 in notin: 
        wa2 = random.randrange(-48, 48)
    notin.add(wa2) 
    wa3 = random.randrange(-48, 48)
    while wa3 in notin: 
        wa3 = random.randrange(-48, 48)
    return [first, second, first - second, wa1, wa2, wa3]   

def generate_multiplication_easy():
    first = random.randrange(1, 14)
    second = random.randrange(1, 14)
    notin = set()
    notin.add(first*second)
    wa1 = random.randrange(1, 14) * random.randrange(1, 14)
    while wa1 in notin:
        wa1 = random.randrange(1, 14) * random.randrange(1, 14)
    notin.add(wa1)
    wa2 = random.randrange(1, 14) * random.randrange(1, 14)
    while wa2 in notin: 
        wa2 = random.randrange(1, 14) * random.randrange(1, 14)
    notin.add(wa2) 
    wa3 = random.randrange(1, 14) * random.randrange(1, 14)
    while wa3 in notin: 
        wa3 = random.randrange(1, 14) * random.randrange(1, 14)
    return [first, second, first * second, wa1, wa2, wa3]

