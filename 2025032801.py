import turtle
t = turtle.Turtle()

t.shape("turtle")
s = int(input("집의 크기를 입력하세요 : "))
t.forward(s)        #정사각형
t.right(90)
t.forward(s)
t.right(90)
t.forward(s)
t.right(90)

t.forward(s)        #정삼각형
t.right(30)
t.forward(s)
t.right(120)
t.forward(s)
t.home()
