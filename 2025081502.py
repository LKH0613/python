from tkinter import *


shape_size = 2
pen_size = 2
pen_color = "black"
my_tool = "pen"
fill_color = "white"

w, h = 13, 2

def clear_canvas() :
    canvas.delete("all")

def change_size(btn):
    global pen_size
    if btn == "plus":
        pen_size += 1
    else:
        if pen_size > 2:
            pen_size -= 1

def change_color(color):
    global pen_color, fill_color, my_tool
    if my_tool == "pen":
        pen_color = color
        btn_pen['bg'] = color
        if color == "white" or color == "yellow":
            btn_pen['fg'] = "black"
        if color == "black":
            btn_pen['fg'] = "white"

    elif my_tool == "canvas":
        canvas['bg'] = color
        btn_canvas['bg'] = color
        if color == "white" or color == "yellow":
            btn_canvas['fg'] = "black"
        if color == "black":
            btn_canvas['fg'] = "white"

    else:
        fill_color = color
        btn_fill['bg'] = color
        if color == "white" or color == "yellow":
            btn_fill['fg'] = "black"
        if color == "black":
            btn_fill['fg'] = "white"

def paint(event):
    global pen_size
    x1, y1 = event.x, event.y
    x2, y2 = event.x + pen_size, event.y + pen_size
    canvas.create_line(x1, y1, x2, y2, width = pen_size, fill = pen_color)

def draw_shape(event):
    global shape_size, my_tool
    x1, y1 = event.x, event.y
    x2, y2 = event.x + shape_size, event.y + shape_size
    if my_tool == "oval":
        canvas.create_oval(x1 - (shape / 2), y1, x2 - (shape_size / 2), y2, fill = fill_color)
    elif my_tool == "rect":
        canvas.create_rectangle(x1, y1, x2, y2, fill = fill_color)
    elif my_tool == "tri":
        canvas.create_polygon(x1, y1, x2, y2, (x1 - (shape-size)), y2, fill= fill_color, outline= "black")

win = Tk()
win.title("My paint")

win.geometry("510x600+200+200")

canvas = Canvas(win, width = 510, height = 470, bg = "white")

Button(win, width = w, height = h)

btn_white = Button(win, bg = "white", width = w, height = h, command = lambda:change_color("white"))
btn_black = Button(win, bg = "black", width = w, height = h, command = lambda:change_color("black"))
btn_blue = Button(win, bg = "blue", width = w, height = h, command = lambda:change_color("blue"))
btn_green = Button(win, bg = "green", width = w, height = h, command = lambda:change_color("green"))
btn_yellow = Button(win, bg = "yellow", width = w, height = h, command = lambda:change_color("yellow"))
btn_red = Button(win, bg = "red", width = w, height = h, command = lambda:change_color("red"))

btn_canvas = Button(win, text = "canvas\ncolor", bg = "white", fg = "black", width = w, height = h, command = lambda : change_tool("canvas"))
btn_pen = Button(win, text = "pen\ncolor", bg = "black", fg = "white", width = w, height = h, command = lambda : change_tool("pen"))
btn_fill = Button(win, text = "fill\ncolor", bg = "white", fg = "black", width = w, height = h, command = lambda : change_tool("shape"))

btn_oval = Button(win, text = "○", bg = "white", width = w, height = h, command = lambda : change_tool("oval"))
btn_rect = Button(win, text = "□", bg = "white", width = w, height = h, command = lambda : change_tool("rect"))
btn_tri = Button(win, text = "△", bg = "white", width = w, height = h, command = lambda : change_tool("tri"))

btn_plus = Button(win, text = "+", width = w, height = h, command = lambda:change_size("plus"))
btn_minus = Button(win, text = "-", width = w, height = h, command = lambda:change_size("minus"))
btn_clear = Button(win, text = "clear", width = w, height = h, command = clear_canvas)

canvas.grid(row = 0, column = 0, columnspan = 6)
btn_canvas.grid(row = 1, column = 0)
btn_black.grid(row = 1, column = 1)
btn_blue.grid(row = 1, column = 2)
btn_green.grid(row = 1, column = 3)
btn_plus.grid(row = 1, column = 4)
btn_pen.grid(row = 2, column = 0)
btn_white.grid(row = 2, column = 1)
btn_red.grid(row = 2, column = 2)
btn_yellow.grid(row = 2, column = 3)
btn_minus.grid(row = 2, column = 4)

btn_fill.grid(row = 3, column = 0)
btn_oval.grid(row = 3, column = 1)
btn_rect.grid(row = 3, column = 2)
btn_tri.grid(row = 3, column = 3)
btn_clear.grid(row = 3, column = 4)

canvas.bind("<B1-Motion>", paint)

win.mainloop()






