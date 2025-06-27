from tkinter import *
from random import * 
win = Tk()

def game(com, user):
    if user ==0:
        if com==0 :
            lbl_res['text']= "Draw"
        elif com == 1:
            lbl_res['text']= "Computer wins!"
        else:
            lbl_res['text']= "User wins!"
    elif user ==1:
        if com==0 :
            lbl_res['text']= "User wins!"
        elif com == 1:
            lbl_res['text']= "Draw"
        else:
            lbl_res['text']= "Computer wins!"
    if user ==2:
        if com==0 :
            lbl_res['text']= "Computer wins!"
        elif com == 1:
            lbl_res['text']= "User wins!"
        else:
            lbl_res['text']= "Draw"

def change_img(user):
    List = ["scissors.png", "rock.png", "paper.png"]

    com = randint(0, 2)

    com_img = PhotoImage(file = List[com])
    user_img = PhotoImage(file = List[user])

    lbl_com['image'] = com_img
    lbl_com.image = com_img
    lbl_user['image'] = user_img
    lbl_user.image = user_img

    game(com, user)

win.title("Rock Paper Scissors Game")

basic_img = PhotoImage(file = "ready.png")
lbl_com = Label(win, image = basic_img, relief = "solid")
lbl_user = Label(win, image = basic_img, relief = "solid")

lbl_res = Label(win, text=' ', width=15, font = ("consolas", 20))

lbl_name1 = Label(win, text = "Computer", font = ("consolas", 20))
lbl_name2 = Label(win, text = "User", font = ("consolas", 20))

btn_scissor = Button(win, text = "scissors", width=15, font=("consolas", 15), command = lambda : change_img(0))
btn_rock = Button(win, text = "rock", width=15, font=("consolas", 15), command = lambda : change_img(1))
btn_paper = Button(win, text = "paper", width=15, font=("consolas", 15), command = lambda : change_img(2))

lbl_com.grid(row = 0, column = 0)
lbl_res.grid(row = 0, column = 1)
lbl_user.grid(row = 0, column = 2)
lbl_name1.grid(row = 1, column = 0)
lbl_name2.grid(row = 1, column = 2)
btn_scissor.grid(row = 2, column = 0)
btn_rock.grid(row = 2, column = 1)
btn_paper.grid(row = 2, column = 2)


win.mainloop()

'''
from tkinter import *
def Click(shape):
    if shape == "circle":
        img = PhotoImage(file = "circle.png")
    elif shape == "triangle":
        img = PhotoImage(file = "triangle.png")
    else:
        img = PhotoImage(file = "star.png")

    lbl["image"] = img
    lbl.image = img
win = Tk()
img = PhotoImage(file = "circle.png")
lbl = Label(win, image = img)
btn1 = Button(win, text = "circle", command = lambda : Click("circle"))
btn2 = Button(win, text = "triangle", command = lambda : Click("triangle"))
btn3 = Button(win, text = "star", command = lambda : Click("star"))
lbl.grid(row=0, column = 0, columnspan = 3)
btn1.grid(row=1, column = 0)
btn2.grid(row=1, column = 1)
btn3.grid(row=1, column = 2)
win.mainloop()
'''
'''
from tkinter import *
def Click(n):
    if n == 1 :
        lbl['text'] = "First button clicked"
    elif n == 2:
        lbl['text'] = "Second  button clicked"
    else :
        lbl['text'] = "Third button clicked"

win = Tk()
lbl = Label(win, text="이름")
btn1 = Button(win, text = "First", command = lambda : Click(1))
btn2 = Button(win, text = "Second", command = lambda : Click(2))
btn3 = Button(win, text = "Third", command = lambda : Click(3))

lbl.grid(row = 0, column = 0, columnspan = 3)
btn1.grid(row = 1, column = 0)
btn2.grid(row = 1, column = 1)
btn3.grid(row = 1, column = 2)
win.mainloop()
'''
