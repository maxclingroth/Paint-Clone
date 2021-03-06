import tkinter as tk

BLACK = '#000000'
WHITE = '#ffffff'
RED = '#f00800'
BLUE = '#1904ff'
GREEN = '#1ba306'
PURPLE = '#8703fa'
ORANGE = '#ff7403'


class Paint:
    def __init__(self):
        self.master = tk.Tk()
        self.master.title('Not MS Paint')
        self.master.geometry('750x750')
        self.w = tk.Canvas(self.master, width=650, height=750, bg=WHITE, cursor='circle')
        self.menu = tk.Frame(self.master)
        self.colorOptions = tk.Frame(self.menu, pady=25)
        self.colorLabel = tk.Label(self.colorOptions, text='Color')
        self.colorLabel.pack()
        self.colorVar = tk.IntVar(value=1)
        self.black = tk.Radiobutton(self.colorOptions, text='Black', variable=self.colorVar, value=1, command=self.changeColor)
        self.red = tk.Radiobutton(self.colorOptions, text='Red', variable=self.colorVar, value=2, command=self.changeColor)
        self.blue = tk.Radiobutton(self.colorOptions, text='Blue', variable=self.colorVar, value=3, command=self.changeColor)
        self.green = tk.Radiobutton(self.colorOptions, text='Green', variable=self.colorVar, value=4, command=self.changeColor)
        self.purple = tk.Radiobutton(self.colorOptions, text='Purple', variable=self.colorVar, value=5, command=self.changeColor)
        self.orange = tk.Radiobutton(self.colorOptions, text='Orange', variable=self.colorVar, value=6, command=self.changeColor)
        self.eraser = tk.Radiobutton(self.colorOptions, text='Eraser', variable=self.colorVar, value=0, command=self.changeColor)
        self.black.pack()
        self.red.pack()
        self.blue.pack()
        self.green.pack()
        self.purple.pack()
        self.orange.pack()
        self.eraser.pack()
        self.colorOptions.pack(side='top')
        self.sizeOptions = tk.Frame(self.menu, pady=25)
        self.sizeLabel = tk.Label(self.sizeOptions, text='Brush Size')
        self.sizeLabel.pack()
        self.sizeVar = tk.IntVar(value=25)
        self.brushSize = tk.Scale(self.sizeOptions, from_=1, to=50, orient='horizontal', variable=self.sizeVar, command=self.changeSize)
        self.brushSize.pack()
        self.sizeOptions.pack()
        self.shapeOptions = tk.Frame(self.menu, pady=25)
        self.shapeLabel = tk.Label(self.shapeOptions, text='Shapes')
        self.shapeLabel.pack()
        self.shapeVar = tk.IntVar(value=0)
        self.circle = tk.Radiobutton(self.shapeOptions, text='Circle', variable=self.shapeVar, value=1, command=self.changeShape)
        self.triangle = tk.Radiobutton(self.shapeOptions, text='Line', variable=self.shapeVar, value=2, command=self.changeShape)
        self.rectangle = tk.Radiobutton(self.shapeOptions, text='Rectangle', variable=self.shapeVar, value=3, command=self.changeShape)
        self.none = tk.Radiobutton(self.shapeOptions, text='None', variable=self.shapeVar, value=0, command=self.changeShape)
        self.circle.pack()
        self.triangle.pack()
        self.rectangle.pack()
        self.none.pack()
        self.shapeOptions.pack()
        self.menu.pack(side='right')
        self.color = BLACK
        self.size = 25
        self.shape = 'none'
        self.x0 = 0
        self.y0 = 0
        self.w.bind('<Button-1>', self.click)
        self.w.bind('<B1-Motion>', self.drag)
        self.w.bind('<ButtonRelease-1>', self.release)
        self.w.pack(side='left')
        self.master.mainloop()

    def changeColor(self):
        if self.colorVar.get() == 0:
            self.color = WHITE
        elif self.colorVar.get() == 1:
            self.color = BLACK
        elif self.colorVar.get() == 2:
            self.color = RED
        elif self.colorVar.get() == 3:
            self.color = BLUE
        elif self.colorVar.get() == 4:
            self.color = GREEN
        elif self.colorVar.get() == 5:
            self.color = PURPLE
        elif self.colorVar.get() == 6:
            self.color = ORANGE

    def changeSize(self, brushSize):
        self.size = int(brushSize)

    def changeShape(self):
        if self.shapeVar.get() == 0:
            self.shape = 'none'
        elif self.shapeVar.get() == 1:
            self.shape = 'circle'
        elif self.shapeVar.get() == 2:
            self.shape = 'line'
        elif self.shapeVar.get() == 3:
            self.shape = 'rectangle'

    def createCircle(self, x, y, r, fill):
        self.w.create_oval(x-r, y-r, x+r, y+r, fill=fill, outline=fill)

    def click(self, event):
        if self.shape == 'none':
            self.createCircle(event.x, event.y, (self.size / 2), self.color)
        else:
            self.x0 = event.x
            self.y0 = event.y

    def drag(self, event):
        if self.shape == 'none':
            self.createCircle(event.x, event.y, (self.size / 2), self.color)

    def release(self, event):
        if self.shape == 'circle':
            self.w.create_oval(self.x0, self.y0, event.x, event.y, outline=self.color, width=(self.size/2))
        elif self.shape == 'line':
            self.w.create_line(self.x0, self.y0, event.x, event.y, fill=self.color, width=(self.size/2))
        elif self.shape == 'rectangle':
            self.w.create_rectangle(self.x0, self.y0, event.x, event.y, outline=self.color, width=(self.size/2))


paint = Paint()
