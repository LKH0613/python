from tkinter import *
from PIL import ImageTk
win = Tk()

def message(event) :
    lbl['text'] = entry.get()
    entry.delete(0, END)

entry = Entry(win)
entry.bind("<Return>", message)
entry.pack()
lbl = Label(win, text = "")
lbl.pack()
win.mainloop()


'''
def click():
    if lbl['text'] == "Hello":
        lbl['text'] = "Python"
        lbl['bg'] = "green"
        lbl['fg'] = "red"
    else :
        lbl['text'] = "Hello"
        lbl['bg'] = "orange"
        lbl['fg'] = "blue"
lbl = Label(win, text = "Hello",fg = "blue", bg = "orange")
btn = Button(win, text= "Button", command=click)
lbl.pack()
btn.pack()

win.mainloop()
'''
'''
img = ImageTk.PhotoImage(file = "JJAJANG.jpg")
lbl = Label(win, image = img)
lbl.pack()
win.mainloop()
'''
'''
win = Tk()
List = ["info", "warning", "error", "question", "questhead", "hourglass", "gray12", "gray25", "gray50", "gray75"]
for i in range(10):
    lbl = Label(win, bitmap = List[i])
    lbl.pack(side = "left")

win.mainloop()
'''
'''
lbl1 = Label(win, text = "orange", width = 20, height = 3, relief = "solid")
lbl2 = Label(win, text = "banana", font = ("Elephant", 20), bg = "yellow")
lbl3 = Label(win, text = "apple", fg = "red")
lbl1.pack()
lbl2.pack()
lbl3.pack()
win.mainloop()
'''

'''
label1 = Label(win, text = "one")
label2 = Label(win, text = "two")
label3 = Label(win, text = "three")
label3.pack()
label2.pack()
label1.pack()
win.mainloop
'''
'''
win.title("C3 coding")
win.geometry("300x200+100+100")
win.resizable(True, False)
win.mainloop()
'''
