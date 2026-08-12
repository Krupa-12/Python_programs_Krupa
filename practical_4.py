#
def welcome():
    print("Welcome to Python Programming!")

welcome()

#output:
''' Welcome to Python Programming!'''

def display(name, age):
    print("Name:", name)
    print("Age:" age)
display("Sahaja", 20)

#output:
'''Name: Sahaja
    Age: 20'''

def sub(a, b):
    return a - b
result = sub(15, 10)
print("Sub =", result)

#output:
''' Sub = 5 '''

def interest(principal, rate=5, time=2):
    si = (principal * rate * time) / 100
    return si
print("Interest =", interest(10000))
print("Interest =", interest(10000, 8, 3))

#output:
''' Interest = 1000.0
    Interest = 2400.0'''

def student(name, age, course):
    print("Name:", name)
    print("Age:", age)
    print("Course:", course)
student(course="Python", name="John", age=21)

#output:
''' Name: John
    Age: 21
    Course: Python'''

def total(*numbers):
    print("Numbers:", numbers)
    print("Sum =", sum(numbers))
total(10, 20, 30)
total(5, 10, 15, 20, 25)

#output:
'''Numbers: (10, 20, 30)
    Sum = 60
    Numbers: (5, 10, 15, 20, 25)
    Sum = 75 '''

import math
num = 25
print("Square Root:", math.sqrt(num))
print("Power:", math.pow(5, 3))
print("Ceiling:", math.ceil(4.2))
print("Floor:", math.floor(4.8))
print("Factorial:", math.factorial(5))
print("Value of Pi:", math.pi)

#output:
'''Square Root: 5.0
    Power: 125.0
    Ceiling: 5
    Floor: 4
    Factorial: 120
    Value of Pi: 3.141592653589793 '''

import random
print("Random Integer:", random.randint(1, 100))
colors = ["Red", "Blue", "Green", "Yellow"]
print("Random Choice:", random.choice(colors))
random.shuffle(colors)
print("Shuffled List:", colors)
print("Random Float:", random.random())

#output:
''' Random Integer: 35
    Random Choice: Blue
    Shuffled List: ['Red', 'Yellow', 'Blue', 'Green']
    Random Float: 0.10480476172160547'''

import statistics
data = [10, 20, 30, 40, 50]
print("Mean:", statistics.mean(data))
print("Median:", statistics.median(data))
print("Mode:", statistics.mode(data))
print("Standard Deviation:", statistics.stdev(data))

#output:
'''Mean: 30
    Median: 30
    Mode: 10
    Standard Deviation: 15.811388300841896'''
