from random import *
import turtle

house = turtle.Turtle()

house.fillcolor('royalblue')

line = turtle.Turtle()

t = turtle.Turtle(shape = 'turtle')

g = turtle.Turtle()

g.write('씨큐브 코딩의 타자 게임!', True, font = ('Arial', 20, 'bold'))
#목록
fruit = ['apple', 'banana', 'strawberry', 'watermelon', 'mandarin', 'peach','grapes', 'Orange', 'pear', 'Kiwi']
#점수
score = 0
#타자 입력 횟수
n = randint(5, 10)

for i in range(n) :
    s = choice(fruit)
    #word변수에 저장
    #입력창 fruit
    #보여줄 내용: 과일명(현재 횟수 / 전체 횟수)
    word = turtle.textinput("fruit", '%s(%d/%d)'% (s, i+1, n))
    if s == word :
        score += 1

#정확도
rate = score / n * 100

g.penup()
g.goto(0, -50)
g.pendown()

#성공 횟수 출력
g.write('%d/%d번 성공!' %(score, n), True, font = ('Arial', 15, 'bold'))
g.penup()
g.goto(0, -100)
g.pendown()

#정확도 출력
g.write('정확도 : %.1f%%' %rate, True, font = ('Arial', 15, 'bold'))

distance = t.distance(line)/100 * rate      #잘못됨
t.speed(1)
#거북이 집에 가기 - 계산한 거리만큼 이동 
t.forward(distance)
# 정확도 100
if rate == 100 :
    t.write('집에 데려다줘서 고마워!! ♬', False, 'center', font = ('Arial', 15, 'bold'))
    t.left(60)
    t.right(60)
    t.left(60)
    t.right(60)

elif rate >= 50:
    t.write("집이 코앞인데!! 한 번만 더 시도 해줘!!", False, 'center', font = ('Arial', 15, 'normal'))

elif rate >= 50:
    t.write("집에 가고 싶어 ㅠ0ㅠ", False, 'center', font = ('Arial', 15, 'normal'))

else:
    t.color('black')
    t.right(360)
    t.write('거북이가 쓰러졌어요 ㅠ_ㅠ', False, 'center', font = ('Arial', 15, 'normal'))
    
turtle.done
'''
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = choices(a, [2, 2, 2, 2, 2, 2, 1, 2, 2, 2,] ,k = 3)
print(b)

if b[0] == 7 and b[1] == 7 and b[2] == 7 :
    print('Lucky!')

    
elif b[0] == 7 :
    if b[1] == 7 or b[2] == 7 :
        print('Good~')
    else :
        print('Soso.')

elif b[1] == 7 :
    if b[2] == 7 :
        print('Good~')
    else :
        print('Soso.')

else :
        print('Soso.')

a = ['apple', 'banana', 'grape', 'kiwi']
print(choice(a))

a = [0, 1]
print(choices(a, [1, 1], k = 1000))

a = [1, 2, 3, 4, 5]
print(choices(a, [10000, 10000, 10000, 10000, 1], k = 200))

print(choices(a, [10000, 10000, 10000, 10000, 1]))

a = choice('abcdefg')
print(a)

t = (1, 2, 3, 4, 5)
a = choice(t)
print(a)

a = ['월', '화', '수', '목', '금', '토', '일']
print(choice([True, False]))
print(choices(a))
'''
