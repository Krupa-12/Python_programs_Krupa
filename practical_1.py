#
a = 9
b = 6
x = 5.55
name = "Python"
flag = True
print("~~~~~~ VARIABLES AND DATA TYPES ~~~~~~")
print("a =", a, "Type:", type(a))
print("b =", b, "Type:", type(b))
print("x =", x, "Type:", type(x))
print("name =", name, "Type:", type(name))
print("flag =", flag, "Type:", type(flag))
#output:
'''~~~~~~ VARIABLES AND DATA TYPES ~~~~~~
   a = 9 Type: <class 'int'>
   b = 6 Type: <class 'int'>
   x = 5.55 Type: <class 'float'>
   name = Python Type: <class 'str'>
   flag = True Type: <class 'bool'>'''

a=int(input("enter a:"))
b=int(input("enter b:"))
print("\n~~~~~~ ARITHMETIC OPERATORS ~~~~~~")
print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
print("a // b =", a // b)
print("a % b =", a % b)
print("a ** b =", a ** b)
#output:
'''enter a:5
   enter b:2
   ~~~~~~ ARITHMETIC OPERATORS ~~~~~~
   a + b = 7
   a - b = 3
   a * b = 10
   a / b = 2.5
   a // b = 2
   a % b = 1
   a ** b = 25'''

print("\n~~~~~~ ASSIGNMENT OPERATORS ~~~~~~")
c = 9
print("Initial c =", c)
c += 6
print("c += 5 =", c)
c -= 3
print("c -= 3 =", c)
c *= 2
print("c *= 2 =", c)
c /= 3
print("c /= 3 =", c)
#output:
'''~~~~~~ ASSIGNMENT OPERATORS ~~~~~~
   Initial c = 9
   c += 5 = 15
   c -= 3 = 12
   c *= 2 = 24
   c /= 4 = 8.0'''

print("\n~~~~~~ COMPARISON OPERATORS ~~~~~~")
a=int(input("enter a:"))
b=int(input("enter b:"))
print("a == b :", a == b)
print("a != b :", a != b)
print("a > b  :", a > b)
print("a < b  :", a < b)
print("a >= b :", a >= b)
print("a <= b :", a <= b)
#output:
'''~~~~~~ COMPARISON OPERATORS ~~~~~~
   enter a:4
   enter b:4
   a == b : True
   a != b : False
   a > b  : False
   a < b  : False
   a >= b : True
   a <= b : True'''

print("\n~~~~~~ LOGICAL OPERATORS ~~~~~~")
p = True
q = False
print("p and q =", p and q)
print("p or q =", p or q)
print("not p =", not p)
#output:
'''~~~~~~ LOGICAL OPERATORS ~~~~~~
   p and q = False
   p or q = True
   not p = False'''

print("\n~~~~~~ MEMBERSHIP OPERATORS ~~~~~~")
   text = "Python Programming"
   print("'Python' in text =", "Python" in text)
   print("'Java' in text =", "Java" in text)
   print("'Java' not in text =", "Java" not in text)
#output:
'''~~~~~~ MEMBERSHIP OPERATORS ~~~~~~
    'Python' in text = True
    'Java' in text = False
    'Java' not in text = True'''

print("\n~~~~~~ IDENTITY OPERATORS ~~~~~~")
list1 = [1, 2, 3]
list2 = list1
list3 = [1, 2, 3]
print("list1 is list2 =", list1 is list2)
print("list1 is list3 =", list1 is list3)
print("list1 is not list3 =", list1 is not list3)
#output:
'''~~~~~~ IDENTITY OPERATORS ~~~~~~
    list1 is list2 = True
    list1 is list3 = False
    list1 is not list3 = True'''

print("\n~~~~~~ BITWISE OPERATORS ~~~~~~")
m=int(input("enter m:"))
n=int(input("enter n:"))
print("m & n =", m & n)
print("m | n =", m | n)
print("m ^ n =", m ^ n)
print("~m =", ~m)
print("m << 1 =", m << 1)
print("m >> 1 =", m >> 1)
#output:
'''~~~~~~ BITWISE OPERATORS ~~~~~~
    enter m:5
    enter n:2
    m & n = 0
    m | n = 7
    m ^ n = 7
    ~m = -6
    m << 1 = 10
    m >> 1 = 2'''