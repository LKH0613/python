def season(n):
    if n == 3 <= n <= 5:
        print("Spring")
    elif n == 6 <= n <= 8:
        print("Summer")
    elif n == 9 <= n <= 11:
        print("Fall")
    elif n == 1 or n == 2 or n == 12:
        print("Winter")
    else:
        print("ERROR")
m = int(input())
season(m)
'''
def judge(n):
    if n >0:
        print("plus")
    elif n < 0:
        print("minus")
    else :
        print("zero")
n = int(input())
judge(n)
'''

'''
def fac(n):
    if n == 1:
        return 1
    else :
        return n * fac(n - 1)
n = int(input())

fact = fac(n)
print(fact)
'''

'''
def factorial(n):
    s = 1
    for i in range(1,n+1):
        s = s * i
    return s

n = int(input())

print(factorial(n))
'''     

'''
def f(n):
    if n > 1 :
        f(n-1)
    print(n)

a = int(input())
f(a)
'''

'''
def A() :
    print(1)
    r = B()
    print(r)

def B() :
    print(2)
    return 3
A()
print(4)
'''

'''
a = 0
def f():
    global a
    global b
    print(a)
    a = 10
    b = 20
f()
print(a)
print(b)
'''

'''
def say(name):
    print("Welcome,", name)
    return
say("Minsu")

def day(m, d):
    print("Today is %s/%s" %(m, d))
m = int(input())
s = int(input())
day(m, s)
'''

'''
from random import *
def random_number() :
    num = random() + 10
    return num
print(random_number())
'''

'''
def warning():
    for i in range(3):
        print("Fire!")

warning()
'''

'''
def two_times() :
    for i in range(1, 10):
        print("2 * %d = %d" % (i, 2 * i))

two_times()
'''
