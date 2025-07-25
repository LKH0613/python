class TV:
    def __init__(self, ch, vol):
        self.channel = ch
        self.volume = vol
        self.power = True


    def on_off(self):
        if self.power:
            self.power = False
            print("Trun off")
        else:
            self.power = True
            print("Trun on")

    def info(self):
        print("Power :", self.power)
        print("Channel :", self.channel)
        print("Volume :", self.volume)

    def set_channel(self, ch):
        if self.power:
            self.channel = ch
        else:
            print("Power off")
            
    def set_volume(self, vol):
        if self.power:
            self.volume = vol
        else:
            print("Power off")

tv = TV(1, 16)
tv.info()
tv.set_channel(5)
tv.on_off()
tv.set_channel(12)
tv.on_off()

'''
from datetime import datetime

print(datetime.today().strftime("%Y년 %m월 %d일"))
print(datetime.today().strftime("%H시 %M분"))
print(datetime.today().strftime("%p %I시 %M분"))
print(datetime.today().strftime("%Y/%m/%d %H:%M:%S"))

now = datetime.now()
time = now.strftime('%p %I시 %M분')
time_kor = time.replace('AM', "오전").replace('PM', '오후')
print(time_kor)
'''
'''
def double_click(event):
    index = listbox.curselection()
    lbl['text'] = listbox.get(index[0])
    
fruit = ["Orange", "Apple","Lemon", "Lime"]

win = Tk()

listbox = Listbox(win)

lbl = Label(win, text = "", bg = "pink", fg = "navy")

for i in range(len(fruit)) :
    listbox.insert(i, fruit[i])
    
listbox.bind("<Double-Button-1>", double_click)

lbl.pack()
listbox.pack()
win.mainloop()
'''
'''
def double_click(event):
    index = listbox.curselection()
    print("Today : ", listbox.get(index[0]))

def left_click(event):
    index = listbox.curselection()
    if index :
        if index[0] == 0:
            print("Yesterday : Sun")
        else:
            print("Yesterday : ", listbox.get(index[0]-1))

def right_click(event):
    index = listbox.curselection()
    if index :
        if index[0] == 6:
            print("Tomorrow : Mon")
        else:
            print("Tomorrow : ", listbox.get(index[0]+1))

day = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
win = Tk()
listbox = Listbox(win)

for i in range(7):
    listbox.insert(i, day[i])

listbox.bind("<Double-Button-1>", double_click)
listbox.bind("<Button-1>", left_click)
listbox.bind("<Button-3>", right_click)

listbox.pack()
win.mainloop()
'''
'''
win = Tk()
listbox = Listbox(win)
for i in range(10) :
    listbox.insert(i, str(i))
print(listbox.curselection())
print(listbox.get(0, 9))
listbox.pack()
win.mainloop()
'''
