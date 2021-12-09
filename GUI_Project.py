#Gavin Chan
import tkinter as tk
from tkinter.constants import CENTER

gui = tk.Tk()
gui.title("GUI Project")
gui.geometry("1200x800")
gui.configure(bg='grey')

def startButtonClick():
    startbutt.place_forget()
    creditbutt.place_forget()
    instructionbutt.place_forget()

    question1 = tk.Label(gui, text = "This is question 1")
    question1.place()

def intructionsButtonClick():
    startbutt.place_forget()
    creditbutt.place_forget()
    instructionbutt.place_forget()
    title.place_forget()
    
    title.configure(text='Instructions')
    title.pack()
    
    intructions = tk.Label(gui, text="These are the intructions", )
    intructions.place(x=100, y=100)


title = tk.Label(gui, text="THE IMPOSSIBLE QUIZ", font=("times",50,"italic"))
title.place(x=250, y=25)

credit = tk.Label(gui, text="By: Gavin Chan \nDaniel Bueno \nJuan Romero", font=("times",12,"italic"))
credit.place(x=1075, y=725)

startbutt = tk.Button(gui, text='START', font=("times",20,"italic"),width=30, height=4, command=startButtonClick)
startbutt.place(x=100, y=300)
#this is just a test idk how this works
creditbutt = tk.Button(gui, text='CREDITS', font=("times",20,"italic"),width=30, height=4)
creditbutt.place(x=100, y=500)
# test number 2
instructionbutt = tk.Button(gui, text='INSTRUCTIONS', font=("times",20,"italic"),width=30, height=4 , command = intructionsButtonClick)
instructionbutt.place(x=645, y=300)

gui.mainloop()
