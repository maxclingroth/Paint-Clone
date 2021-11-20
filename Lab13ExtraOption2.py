#
# Max Clingroth
# 11/16/21
# A program for creating colored blocks in a pattern around a mouse click using tkinter
#

# Import tkinter
from tkinter import *

# Declare constant values
RED = '#8E1B0D'
PURPLE = '#5C04A5'
BLUE = '#3072F5'
# An array telling the placement of each color in the arrangement
COLOR_SPREAD = [[0,0,0,0,0], [0,1,1,1,0], [0,1,2,1,0], [0,1,1,1,0], [0,0,0,0,0]]

# Define a function to handle mouse clicks, which passes the click location to the makeBlocks function
def mouseClick(event):
    makeBlocks(w, event.x, event.y, 30)

# Define a function that creates blocks on the canvas centered around the mouse
def makeBlocks(w, xlocation, ylocation, size):
    for i in range(5):
        for j in range(5):
            w.create_rectangle(getCoordinates(i, j, xlocation, ylocation, size), fill=getColor(i, j))

# A function that calculates the necessary coordinates for each block based on the nested for loop in makeBlocks
def getCoordinates(i, j, xlocation, ylocation, size):
    x1 = (xlocation + (-2.5 + i) * size)
    y1 = (ylocation + (-2.5 + j) * size)
    x2 = (xlocation + (-1.5 + i) * size)
    y2 = (ylocation + (-1.5 + j) * size)
    return x1, y1, x2, y2

# Uses the COLOR_SPREAD list to determine the necessary color for each block
def getColor(x, y):
    if COLOR_SPREAD[x][y] == 0:
        return BLUE
    elif COLOR_SPREAD[x][y] == 1:
        return PURPLE
    else:
        return RED

# Creates the window, the canvas, and binds the mouse click event
master = Tk()
w = Canvas(master, width=1000, height=1000)
w.bind("<Button-1>", mouseClick)
w.pack()

# Runs the program
mainloop()
