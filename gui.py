from tkinter import *
from math import *
import matplotlib.pyplot as plt
import numpy as np

win = Tk()
win.title("Topic - Ground Response Analysis")

def summ():
    def graph():
        H = float(t1.get())
        vs = float(t2.get())
        es = float(t3.get())
        es=es/100
        vr = float(t4.get())
        er = float(t5.get())
        er=er/100
        def f(x,a):
            tt=np.cos(x*a)
            ta=(x*a)
            az=0.15
            return sqrt(1/((tt*tt)+(az*az*(ta*ta))))
        f2 = np.vectorize(f)
        k=(np.pi*2*H)/vs
        xlist = np.arange(0,25,0.001)
        y=f2(xlist,k)
        plt.plot(xlist,y)
        plt.xlabel(r"Frequency(Hz)", size=18)
        plt.ylabel(r"|F(3)|", size=18)
        plt.xlim(0,25)
        plt.ylim(0,10)
        plt.grid()
        plt.show()
    win = Tk()
    win.title("3. Input window")
    win.geometry('500x250')
    l0 = Label(win, text="Input all values", fg="red")
    l0.grid(row=0, column=0)
    l1 = Label(win, text="Depth(H) of soil, in ft")
    l1.grid(row=1, column=0)
    t1 = Entry(win)
    t1.grid(row=1, column=1)
    l2 = Label(win, text="Shear wave velocity of soil(v), in ft/sec")
    l2.grid(row=2, column=0)
    t2 = Entry(win)
    t2.grid(row=2, column=1)
    l3 = Label(win, text="Damping ratio of soil, in %")
    l3.grid(row=3, column=0)
    t3 = Entry(win)
    t3.grid(row=3, column=1)
    l4 = Label(win, text="Shear wave velocity of rock(v), in ft/sec")
    l4.grid(row=4, column=0)
    t4 = Entry(win)
    t4.grid(row=4, column=1)
    l5 = Label(win, text="Damping ratio of rock, in %")
    l5.grid(row=5, column=0)
    t5 = Entry(win)
    t5.grid(row=5, column=1)
    b1 = Button(win, text="Draw Transfer function", command=graph)
    b1.grid(row=6, column=1)


def fun():
    def graph():
        H = float(t1.get())
        vs = float(t2.get())
        ee = float(t3.get())
        e=ee/100
        def f(x,a):
            tt=np.cos(x*a)
            return sqrt(1/((tt*tt)+(e*e*a*a*x*x)))
        f2 = np.vectorize(f)
        k=(np.pi*2*H)/vs
        xlist = np.arange(0,25,0.001)
        y=f2(xlist,k)
        plt.plot(xlist,y)
        plt.xlabel(r"Frequency(Hz)", size=18)
        plt.ylabel(r"|F(2)|", size=18)
        plt.xlim(0,25)
        plt.ylim(0,20)
        plt.grid()
        plt.show()
    win = Tk()
    win.title("2. Input window")
    win.geometry('500x250')
    l0 = Label(win, text="Input all values", fg="red")
    l0.grid(row=0, column=0)
    l1 = Label(win, text="Depth(H), in ft")
    l1.grid(row=1, column=0)
    t1 = Entry(win)
    t1.grid(row=1, column=1)
    l2 = Label(win, text="Shear wave velocity of soil(v), in ft/sec")
    l2.grid(row=2, column=0)
    t2 = Entry(win)
    t2.grid(row=2, column=1)
    l3 = Label(win, text="Damping ratio of soil, in %")
    l3.grid(row=3, column=0)
    t3 = Entry(win)
    t3.grid(row=3, column=1)
    b1 = Button(win, text="Draw Transfer function", command=graph)
    b1.grid(row=4, column=1)


def test():
    def graph():
        H = float(t1.get())
        vs = float(t2.get())
        e = float(t3.get())
        def f(x,a):
            return abs(1/(np.cos(x*a)))
        k=(np.pi*2*H)/vs
        xlist = np.arange(0,25,0.001)
        y=f(xlist,k)
        plt.plot(xlist,y)
        plt.xlabel(r"Frequency(Hz)", size=18)
        plt.ylabel(r"|F(1)|", size=18)
        plt.xlim(0,25)
        plt.ylim(0,20)
        plt.grid()
        plt.show()
    win = Tk()
    win.title("1. Input window")
    win.geometry('500x250')
    l0 = Label(win, text="Input all values", fg="red")
    l0.grid(row=0, column=0)
    l1 = Label(win, text="Depth(H), in ft")
    l1.grid(row=1, column=0)
    t1 = Entry(win)
    t1.grid(row=1, column=1)
    l2 = Label(win, text="Shear wave velocity of soil(v), in ft/sec")
    l2.grid(row=2, column=0)
    t2 = Entry(win)
    t2.grid(row=2, column=1)
    l3 = Label(win, text="Damping ratio of soil, in %")
    l3.grid(row=3, column=0)
    t3 = Entry(win)
    t3.grid(row=3, column=1)
    b1 = Button(win, text="Draw Transfer function", command=graph)
    b1.grid(row=4, column=1)

l1 = Label(win, text="1. Uniform, Undamped Soil layer on Rigid Bedrock ----------------->")
l1.grid(row=0, column=0)
l2 = Label(win, text="2. Uniform, Damped Soil layer on Rigid Bedrock ------------------->")
l2.grid(row=1, column=0)
l3 = Label(win, text="3. Uniform, Damped Soil layer on Elastic Bedrock ----------------->")
l3.grid(row=2, column=0)
l5 = Label(win,text="\n\nMade by - Ved Sharda\nRoll No - 18064019\nCourse - CE491 (UG Project - II)\nGuided by - Dr. Supriya Mohanty\nCivil Engg., IIT BHU",fg="red")
l5.grid(row=4, column=1)

b1=Button(win, text="1. Click here", command=test )
b1.grid(row=0, column=1)
b2 = Button(win, text="2. Click here", command=fun)
b2.grid(row=1, column=1)
b3 = Button(win, text="3. Click here", command=summ)
b3.grid(row=2, column=1)

win.geometry('700x250')
win.mainloop()
