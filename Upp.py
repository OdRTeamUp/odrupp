import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style

from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

LARGE_FONT = ("Verdana", 12)
style.use("ggplot")

f = Figure(figsize=(4,4), dpi=100)
f1 = Figure(figsize=(4,4), dpi=100)
f2 = Figure(figsize=(4,4), dpi=100)
f3 = Figure(figsize=(4,4), dpi=100)

def animate(i):
    a = f.add_subplot(111)
    graph_data = open("/home/pi/Desktop/Up/Valori/temperature.txt", 'r').read()
    lines = graph_data.split('\n')
    xs = []
    ys = []
    l=0
    for line in lines:
        if len(line)>1:
            line=round(float(line),2)
            xs.append(l)
            ys.append(line)
            l=l+1
    a.clear()
    a.plot(xs,ys)
    
def animate1(j):
    a1 = f1.add_subplot(111)
    graph_data1 = open("/home/pi/Desktop/Up/Valori/pressione.txt", 'r').read()
    lines1 = graph_data1.split('\n')
    xs1 = []
    ys1 = []
    l=0
    for line in lines1:
        if len(line)>1:
            line=round(float(line),2)
            xs1.append(l)
            ys1.append(line)
            l=l+1
    a1.clear()
    a1.plot(xs1,ys1)
    
def animate2(k):
    a2 = f2.add_subplot(111)
    graph_data2 = open("/home/pi/Desktop/Up/Valori/umidita.txt", 'r').read()
    lines2 = graph_data2.split('\n')
    xs2 = []
    ys2 = []
    l=0
    for line in lines2:
        if len(line)>1:
            line=round(float(line),2)
            xs2.append(l)
            ys2.append(line)
            l=l+1
    a2.clear()
    a2.plot(xs2,ys2)
    
def animate3(h):
    a3 = f3.add_subplot(111)
    graph_data3 = open("/home/pi/Desktop/Up/Valori/temperature.txt", 'r').read()
    lines3 = graph_data3.split('\n')
    xs3 = []
    ys3 = []
    l=0
    for line in lines3:
        if len(line)>1:
            line=round(float(line),2)
            xs3.append(l)
            ys3.append(line)
            l=l+1
    a3.clear()
    a3.plot(xs3,ys3)

class Upp(tk.Tk):
    
    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "Upp")
        
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        self.frames = {}
        
        frame = StartPage(container, self)
        
        self.frames[StartPage] = frame
        
        frame.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame(StartPage)
        
    def show_frame(self, cont):
        
        frame = self.frames[cont]
        frame.tkraise()
        
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().grid(row=0, column=0, sticky="nsew")
            
        canvas1 = FigureCanvasTkAgg(f1, self)
        canvas1.draw()
        canvas1.get_tk_widget().grid(row=0, column=1, sticky="nsew")
            
        canvas2 = FigureCanvasTkAgg(f2, self)
        canvas2.draw()
        canvas2.get_tk_widget().grid(row=1, column=0, sticky="nsew")
            
        canvas3 = FigureCanvasTkAgg(f3, self)
        canvas3.draw()
        canvas3.get_tk_widget().grid(row=1, column=1, sticky="nsew")
            

        canvas._tkcanvas.grid(row=0, column=0, sticky="nsew")
        canvas1._tkcanvas.grid(row=0, column=1, sticky="nsew")
        canvas2._tkcanvas.grid(row=1, column=0, sticky="nsew")
        canvas3._tkcanvas.grid(row=1, column=1, sticky="nsew")

            
app = Upp()
ani = animation.FuncAnimation(f, animate, interval=1000)
ani1 = animation.FuncAnimation(f1, animate1, interval=1000)
ani2 = animation.FuncAnimation(f2, animate2, interval=1000)
ani3 = animation.FuncAnimation(f3, animate3, interval=1000)
app.mainloop()
