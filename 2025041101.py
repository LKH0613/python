t1 = (1,)
t2 = (2, 3, 4)
print(t1 + t2)


l1 = ['a','b','c','c','d','e','a']
s1 = set(l1)
print(s1)

d1 = {'a' : 90, 'b' : 85, 'c' : 95}
d1['e'] = 70
d1['a'] = 100
print(d1)
'''
import turtle
t = turtle.Turtle()
s = '즐거운 씨큐브 코딩'
n = turtle.numinput(s, '앞으로 얼마나 이동할까요?')
t.forward(n)
ang = turtle.numinput(s, '오른쪽으로 얼마나 회전할까요? :', default = 0, min val = 0, maxval = 360)
t.right(ang)
turtle.done()

a = set([1, 2, 3])
a.add(4)
print(a)
a.update('abc')
print(a)
a.remove('c')
print(a)

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])
print(s1 - s2)
print(s1 & s2)
print(s1 | s2)


d = {'a' : 1, 'b' : 2}
d['c'] = 3
del d['a']
print(d)

a = [1, 2, 3]

del a[0]

print(a)

del a[0]

print(a)

a = 'Carpe Diem!'
b = [1, 2, 3, 4, 5, 6]
print(len(a))
print(len(b))

t1 = (1,)
t2 = (4, 5, 6)
print(t1 + t2)
print(t2 * 2)
print(t2[0])
print(t2[1:3])
    

a = 1

print(a)

a += 1

print(a)

a *= 2

print(a)

t1 = ()
t2 = (1,)
t3 = (1, 2, 3)
t4 = (1, 2,(3, 4))

print(t1)
print(t2)
print(t3)
print(t4)



d = {'name' : 'Jane', 'age' : 12, 'number' : 123456}
print(d)

s1 = set([1, 2, 3])
s2 = set('apple')
print(s1)
print(s2)
'''
