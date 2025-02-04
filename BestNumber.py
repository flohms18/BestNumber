import random

def BestNumber():
    x = random.randint(1,100)
    y = random.randint(1,100)
    z = random.randint(1,100)
    
    MyArray = [x, y, z]
    

    print(f"x = {x}, y = {y}, z = {z}")
    
    largest = max(MyArray)
    print(f"The largest number is {largest}")

    

BestNumber()