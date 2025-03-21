import turtle
t = turtle.Turtle()

t.shape("turtle")
s = int(input("집의 크기를 입력하세요 : "))
t.forward(s)
t.right(90)
t.forward(s)
t.right(90)
t.forward(s)
t.right(90)        #정사각형

t.forward(s)       #정삼각형
t.right(60)

t.forward(s)
t.right(60)
t.forward(s)
t.right(60)        #여기 까지




'''
t.shape("turtle")
r = 50
t.circle(r)
t.penup()
t.goto(100, 0)
t.pendown()
r = 80
t.circle(r)
t.penup()
t.goto(200,0)
t.pendown()
r = 110
t.circle(r)


r = 50
t.penup()  
t.goto(-200, -r)  
t.pendown()  
t.circle(r)


r = 80
t.penup()
t.goto(-50, -r)  
t.pendown()
t.circle(r)


r = 110
t.penup()
t.goto(150, -r)
t.pendown()
t.circle(r)






















t.speed(1)
t.right(90)
stmp1 = t.stamp()
t.forward(30)
stmp2 = t.stamp()
t.forward(50)
t.undo()
t.clearstamp(stmp1)
t.penup()
t.goto(-20,0)
t.dot(10)
t.goto(20,0)
t.dot(10)
t.goto(15,-40)
t.right(75)
t.pendown()
t.circle(-50,40)


t.shape("turtle")
t.speed(1)
t.forward(100)
t.pencolor("red")
t.left(120)
t.forward(100)
t.pensize(5)
t.left(120)
t.forward(100)
t.penup()
t.goto(-50,86.6)
t.pendown()
t.pen(pensize=10, pencolor= "blue", speed=10)
t.setheading(330)
t.forward(86.6)

t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)

t.right(90)
t.forward(100)
t.right(60)
t.backward(100)
t.right(60)
t.forward(100)


t.goto(120, 100)
t.goto(120, -100)
t.goto(-120, 100)
t.goto(-120, -100)
t.goto(0, 0)
t.done()

t.setx(100)
t.sety(100)
t.setx(0)
t.sety(0)

t.goto(100,0)
t.goto(100,100)
t.goto(0,100)
t.goto(0,0)

t.setheading(120)
t.forward(100)
t.setheading(240)
t.forward(100)
t.home()
'''
turtle.done()
