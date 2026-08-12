#Aim:Implement programs using if, if-else, elif, while loop, for loop, nested loops, and loop control statements (break, continue, pass).

a="hello,python!"
if a != "hello":
  print("Hello,Python!")

#output:
'''Hello,Python!'''

age=int(input("enter your age:"))
if age >= 18:
  print("you are eligible to vote.")
else:
  print("you are not eligible to vote")

#output:
'''enter your age:54
   you are eligible to vote.'''

year=int(input("enter a year:"))
if (year % 4 == 0 and year % 100 != 0):
  print("{0} is a leap year".format(year))
elif (year % 400 == 0 and year % 100 == 0):
  print("{0} is a leap year".format(year))
else:
  print("{0} is not leap year".format(year))

#output:
'''enter a year:2000
   2000 is a leap year'''

i = 1
while i <= 5:
    print(i)
    i += 1

#output:
''' 1
    2
    3
    4
    5'''

for i in range(1, 6):
    print(i)

#output:
''' 1
    2
    3
    4
    5'''

r = int(input("Enter the number of rows: "))
i = 1
while i <= r:
    sp = 1
    while sp <= r - i:
        print(" ", end="")
        sp += 1
    stars = 1
    while stars <= (2 * i - 1):
        print("*", end="")
        stars += 1
    print()
    i += 1

#output:
'''Enter the number of rows: 4
       *
      ***
     *****
    *******'''

r = int(input("Enter the number of rows: "))
for i in range(1, r + 1):
    # Print leading spaces
    for j in range(r - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print()

#output:
'''Enter the number of rows: 4
       *
      ***
     *****
    *******'''

for i in range(1, 11):
    if i == 5:
        break
    print(i)

#output:
''' 1
    2
    3
    4'''

for i in range(1, 11):
    if i == 5:
        continue
    print(i)

#output:
''' 1
    2
    3
    4
    6
    7
    8
    9
    10'''

for i in range(1, 6):
    if i == 3:
        pass
    print(i)

    #output:
''' 1
    2
    3
    4
    5'''
