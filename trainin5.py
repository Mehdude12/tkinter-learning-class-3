import tkinter as share_the_a_screen
from tkinter import *

app = share_the_a_screen.Tk()

app.title("Share-the-event-handeler-screen")
app.geometry("2000x2000")


def handle_keypress(event):
    print(event.char)


app.bind("<Key>", handle_keypress)


def handle_click(event):
    print("YOU JUST DESTROYED A HOMELESS MAN'S HOME THAT HE COULD BARELY AFFORD AFTER 120 YEARS OF HARDWORK OF GENERATIONS WHO DIED OF A HEART ATTACK CAUSED BY SHOCK!! \n ARE YOU PROUD OF YOURSELF NOW?!?!?!?!")


btn1 = Button(
    bg="blue", text="DONT FORGET YOUR DUOLNGO LESSONS OR ILL KILL YOU")

btn1.pack()

btn1.bind("<Button-1>", handle_click)


app.mainloop()
