from tkinter import *
from turtle import *
speed(1000)
width(5)

for i in range (0,30):
  clear()
  color("white")
  home()
  left(i*8)
  forward(50)
  color("red")
  left(90)
  forward(50)
  left(90)
  forward(100)
  left(90)
  forward(100)
  left(90)
  forward(100)
  left(90)
  forward(50)
 
 
root = Tk()
a = Label(root, text="Hello, world!")
a.pack()
root.mainloop()