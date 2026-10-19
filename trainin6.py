import tkinter as share_the_a_screen
from tkinter import *
from tkinter import messagebox

app = share_the_a_screen.Tk()

app.title("Share-the-event-handeler-screen")
app.geometry("2000x2000")


def msg():
    messagebox.showwarning(
        "YOU ARE ABOUT TO BREAK A POOR MAN'S HOUSE!!!!!", "I suggest you do it.")


destroy = Button(text="DESTROY LA HOME", command=msg)

destroy.place(x=40, y=80)


def handle_click(event):
    print("YOU JUST DESTROYED A HOMELESS MAN'S HOME THAT HE COULD BARELY AFFORD AFTER 120 YEARS OF HARDWORK OF GENERATIONS WHO DIED OF A HEART ATTACK CAUSED BY SHOCK!! \n ARE YOU PROUD OF YOURSELF NOW?!?!?!?!")


destroy.bind("<Button-1>", handle_click)


app.mainloop()
