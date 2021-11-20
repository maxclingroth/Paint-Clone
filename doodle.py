import tkinter as tk


class Paint:
    def __init__(self):
        self.master = tk.Tk()
        self.master.geometry('750x750')
        self.w = tk.Canvas(self.master, width=500, height=750)
        self.w.pack(side='left')
        self.menu = tk.Frame(self.master, width=250, height=750)
        self.colorOptions = tk.Frame(self.menu)
        self.colorVar = tk.IntVar(value=1)
        self.black = tk.Radiobutton(self.colorOptions, text='Black', variable=self.colorVar, value=1)
        self.red = tk.Radiobutton(self.colorOptions, text='Red', variable=self.colorVar, value=2)
        self.blue = tk.Radiobutton(self.colorOptions, text='Blue', variable=self.colorVar, value=3)
        self.green = tk.Radiobutton(self.colorOptions, text='Green', variable=self.colorVar, value=4)
        self.purple = tk.Radiobutton(self.colorOptions, text='Purple', variable=self.colorVar, value=5)
        self.orange = tk.Radiobutton(self.colorOptions, text='Orange', variable=self.colorVar, value=6)
        self.eraser = tk.Radiobutton(self.colorOptions, text='Eraser', variable=self.colorVar, value=0)
        self.black.pack()
        self.red.pack()
        self.blue.pack()
        self.green.pack()
        self.purple.pack()
        self.orange.pack()
        self.eraser.pack()
        self.colorOptions.pack()
        self.menu.pack(side='right')
        self.master.mainloop()

    def changeColor(self):
        pass


paint = Paint()
