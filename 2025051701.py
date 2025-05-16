n = int(input("n : "))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end = ' ')
    print()



'''
for i in range(2, 10):
    print("< %d 단 >" % i)
    for j in range(1, 10):
        print("%d x %d = %2d" % (i, j, i*j))

    print()


n = int(input())
m = int(input()) + 1
for i in range(n):
    for j in range(1, m):
        print(j, end = ' ')

    print()
a = int(input())
b = int(input()) + 1

for i in range(a):
    for j in range(b):
        print('*', end = '')
    print()

sum = 0
cnt = 0
while (True):
    n = int(input())

    if n == -1 :
        break

    sum = sum + n
    cnt = cnt + 1
        
print("sum: %d" % (sum))
print('avg: %.2lf' % (sum/cnt))



list = []


while (True):
    n = int(input())

    if n == -1 :
        break

    list.append(n)
    
print("sum: %d" % sum(list))
print('avg: %.2lf' % (sum(list)/len(list)))


sum = 0
for i in range(5):
    n = int(input())
    sum = sum + n
    
print("sum : %d" % (sum))
print("avg : %.2lf" % (sum/5))

n = int(input())

if n > 50:
    for i in range (n, 49, -1):
        print(i, end = ' ')

elif n < 50:
    for i in range (n, 51, 1):
        print(i, end = ' ')

else:
    print(50)

for i in range(10):
    print(i, end = ' ')
    
print()

for i in range(10, 21):
    print(i, end = ' ')
    
print()

for i in range(1, 10, 2):
    print(i, end = ' ')
    
print()

for i in range(3, 100, 3):
    print(i, end = ' ')

print()

List = ['a', 'b' , 'c']
for s in List:
    print(s)

num_list = [3, 42, 34, 45, 35]
sum = 0
for num in num_list:
    sum += num
print("avg : %lf" %(sum/5))

n = int(input()) + 1
for i in range(1, n):
    print(i, end = ' ')

import random

com = random.randint(1, 100)

while (True):
    user = int(input())

    if (com == user):
        print("Correct")
        break

    elif(com > user):
        print("Up")

    else :
        print("Down")

 n = int(input()) + 1
for i in range(1, n):
    print(i, end = ' ')
print()
'''
