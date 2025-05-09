''' 반복문 1
n = int(input('Put Number : '))
Sum = 0
i = 1
while i <= n:
    Sum = Sum + i
    i = i + 1

print(Sum)    
'''

''' 반복문 2
while True:
    ans = input("Shall we close? (Y/N)")
    if ans == 'y' or ans == 'Y' :
        print('Closed')
        break
'''
''' 반복문 3
n = int(input())

Sum = 0
i = 1

while True:
    Sum = Sum + i
    i = i + 1
    if i>n:
        break

print(Sum)
'''
'''
n = int(input())
i = 0
while i < n :
    i += 1
    if i % 2 == 0 :
        continue

    if i > n :
        break
    print(i, end = ' ')
'''
'''
n = int(input())
i = 0
while i < n :
    i += 1

    if i >= n :
        break
    
    if i % 2 == 0 :
        print(i, end = ' ')
'''
'''
ans = ''
while ans != 'Yes':
    ans = input('Are you ready')
    if ans == 'Yes':
        print('Going out')
        break
'''
'''
while True:
    ans = input("Are you ready")

    if ans == 'Yes':
        print("Going out")
        break
'''
'''
i = 0
while i < 5:
    
    n = int(input("input: "))
    i = i + 1
    if n % 5 == 0:
        continue
    print("output: %d" % (n))

    
    
'''
'''
    i = 0
while True:
    
    n = int(input("input: "))
    i = i + 1
    if n % 5 == 0:
        continue
    print("output: %d" % (n))
    if i > 5:
        break
'''
'''#거듭제곱근 계산기
n = int(input())
m = int(input())
a = n ** (1/m)
print(a)
'''
'''
m = 0
while True:
    n = int(input())
    m = m + n
    if n == 0:
        break
print("output: %d"% (m))
'''
'''
a = []

while True:
    n = int(input())

    if n == 0:
        break

    a.append(n)

print("output: %d"% sum (a))
'''
'''
cnt = 0
n = int(input("정수 입력: "))
while n > 0:
    cnt += 1
    n //= 10
print("자릿수: %d"% cnt)
'''
'''
n = int(input())
'''
'''
ans = 0

n = int(input("정수 입력:"))

while True:
    ans = ans + n % 10
    n = n // 10
    if n == 0 :
        break
    ans = ans * 10
print('뒤집은 수:%d'% ans)
'''

import sys
import pygame
from pygame. locals import *

pygame.init()

screen = pygame.display.set_mode((400,300))

pygame.display.set_caption("Tick Tock Timer")

CLOCK = pygame.time.Clock()

sysfont = pygame.font.SysFont(None, 36)

timer = 0
while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    timer += 1

    screen.fill((255, 255, 255))

    cnt_txt = sysfont.render("Timer: %d"% timer, True, (0, 0, 0))

    screen.blit(cnt_txt, (140,140))

    pygame.display.update()

    CLOCK.tick(50)
