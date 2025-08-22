from tkinter import *

win = Tk()
win.title("계산기")
win.geometry("480x600+300+300")
win.resizable(False, False)

w, h = 16, 2

# 길이 / 상단

btn_meter = Button(win, width = w, height = h, text = "m")
btn_inch = Button(win, width = w, height = h, text = "in")
btn_mile = Button(win, width = w, height = h, text = "mile")
btn_yard = Button(win, width = w, height = h, text = "yd")

btn_meter.grid(row = 0, column = 0)
btn_inch.grid(row = 0, column = 1)
btn_mile.grid(row = 0, column = 2)
btn_yard.grid(row = 0, column = 3)

#무게 / 상단

btn_gram = Button(win, width = w, height = h, text = "g")
btn_kilogram = Button(win, width = w, height = h, text = "kg")
btn_lbs = Button(win, width = w, height = h, text = "lbs")
btn_oz = Button(win, width = w, height = h, text = "oz")

btn_gram.grid(row = 1, column = 0)
btn_kilogram.grid(row = 1, column = 1)
btn_lbs.grid(row = 1, column = 2)
btn_oz.grid(row = 1, column = 3)

#데이터 / 상단

btn_byte = Button(win, width = w, height = h, text = "B")
btn_megabyte = Button(win, width = w, height = h, text = "MB")
btn_gigabyte = Button(win, width = w, height = h, text = "GB")
btn_terabyte = Button(win, width = w, height = h, text = "TB")

btn_byte.grid(row = 2, column = 0)
btn_megabyte.grid(row = 2, column = 1)
btn_gigabyte.grid(row = 2, column = 2)
btn_terabyte.grid(row = 2, column = 3)



entry_number = Entry(win, width = w)
entry_number.grid(row = 3, column = 2)

lbl_number = Label(win, text = "숫자를 입력하세요")
lbl_number.grid(row = 3, column = 1)
win.mainloop()

