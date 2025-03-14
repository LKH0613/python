'''
a = 1
print(a)
a = 2
print(a)


a = 123
b = "hello world"
c = True
d = 123.456
print(a , type(a))
print(b , type(b))
print(c , type(c))
print(d , type(d))

print("%d은 정수다" % 3)

number = 3.141592

print("%d은 정수다" % number)
print("%lf는 소수이다" % number)

m = 3
d = 14
print("오늘은 %d월 %d일 이다" %(m,d))

g = 1
c = 3
n = 19
print("나는 %s학년 %s반 %s번 이다" %(g,c,n))

pi = 3.141592

print("%fl" % pi)
print("%.2fl" % pi)


a = 1
b = 10
c = 100
d = 2
e = 20
f = 200

print("%-3d %3d" % (a,d))
print("%-3d %3d" % (b,e))
print("%-3d %3d" % (c,f))

name = "이강현"

print("내 이름은 {0}이고 {1}월에 태어났다." .format(name,6))

a = 10
b = 3
print(a/b)
print(a//b)
print(a%b)


name = input("이름: ")
print("==자기 소개하기==")
print("이름 : %s" % name)
'''
a = int(input())
b = int(input())

print("%d + %d = %d , %d x %d = %d" % (a, b, a+b, a+b, b, (a+b)*b))
