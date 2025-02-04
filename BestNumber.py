import random

def BestNumber():
    x = random.randint(1,100)
    y = random.randint(1,100)
    z = random.randint(1,100)

    print(f"x = {x}, y = {y}, z = {z}")

    if x > y and x > z:
        print("x is the best number")
    elif y > x and y > z:
        print("y is the best number")
    else:    
        print("z is the best number")

    

BestNumber()