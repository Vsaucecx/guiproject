#Gavin Chan
import tkinter as tk

gui = tk.Tk()
gui.title("GUI Project")
gui.geometry("1200x800")
gui.configure(bg='grey')



title = tk.Label(gui, text="THE IMPOSSIBLE QUIZ", font=("times",50,"italic"))
title.place(x=250, y=75)

credit = tk.Label(gui, text="By: Gavin Chan \nDaniel Bueno \nJuan Romero", font=("times",12,"italic"))
credit.place(x=1075, y=725)

startbutt = tk.Button(gui, text='START', font=("times",20,"italic"),width=30, height=4)
startbutt.place(x=100, y=300)

creditbutt = tk.Button(gui, text='CREDITS', font=("times",20,"italic"),width=30, height=4)
creditbutt.place(x=100, y=500)

instructionbutt = tk.Button(gui, text='INSTRUCTIONS', font=("times",20,"italic"),width=30, height=4)
instructionbutt.place(x=645, y=300)

gui.mainloop()
