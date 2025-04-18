'''
x = 10
y = 50
print("x : %d, y : %d" %(x, y))
print('x는 y는 같다?', x == y)
print('x는 y는 다르다?', x != y)
print('x는 y보다 크다?', x > y)
print('x는 y보다 작다?', x < y)
print('x는 y보다 크거나 같다?', x >= y)
print('x는 y보다 작거나 같다?', x <= y)

x = True
y = False
print('x : %s, y : %s' %(x, y))
print('x and y =', x and y)
print('x or y =', x or y)
print('not x =', not x)
print('not y =', not y)

if(score >= 90):
    print("A")

print("Pass")
if(score >= 60 and score <= 100):
    print("Pass")
else:
    print("Fail")

if (score >= 90):
    print("A")
elif (score >= 60):
    print("B")
else:
    print("C")

if(score >= 90):
    print("A")
else:
    if(score >= 60):
        if(score <= 89):
            print("B")

score = int(input("score = "))
x = 10
print(x >= 0 and x <= 10)
print(x < 0 or x <= 10)
print(not x)

a = int(input())
b = int(input())
c = int(input())
print(a >= 140 and b >= 140 and c >= 140)

a = int(input())
b = int(input())
c = int(input())
if(a >= 140 and b >= 140 and c >= 140):
    print("True")
else:
    print("False")

n = int(input())

if(n == 0):
    print("ZERO")
elif(n%2):
    print("ODD")
else:
    print("EVEN")

year = int(input("year : "))
#1 (year%4 == 0 and year%100 != 0)
#2 (year%400 == 0)
if(year%4 == 0 and year%100 != 0) or (year%400 == 0):
    print("leap year")
else:
    print("common year")

a = 1 in [1, 2, 3]
print(a)
a = 1 not in [1, 2, 3]
print(a)

n = str(input())
case = ['Homework', 'Eating', 'Sleeping']
if(n in case):
    print('I have to do homework.')
else:
    print("It's break time.")
'''
import random
com = random.randint(1, 2)
user = int(input('odd : 1, even : 2\n'))
print('COM(%d) : USER(%d)' %(com, user))
if (com == user):
    print('correct')
else:
    print('Incorrect')
