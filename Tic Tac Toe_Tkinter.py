from tkinter import *
import tkinter.messagebox
from tkinter import StringVar

tk = Tk()
tk.title('Tic Tac Toe Game')

px = StringVar()
po = StringVar()
p1 = StringVar()
p2 = StringVar()

player1_name = Entry(tk, textvariable=p1, bd=5, width=20)
player1_name.grid(row=0, column=1, columnspan=5)
player2_name = Entry(tk, textvariable=p2, bd=5, width=20)
player2_name.grid(row=1, column=1, columnspan=5)

click_b = True
button_clicked = 0


def disableButton():
    b1.configure(state=DISABLED)
    b2.configure(state=DISABLED)
    b3.configure(state=DISABLED)
    b4.configure(state=DISABLED)
    b5.configure(state=DISABLED)
    b6.configure(state=DISABLED)
    b7.configure(state=DISABLED)
    b8.configure(state=DISABLED)
    b9.configure(state=DISABLED)


def Click_btn(bns):
    global click_b, button_clicked, player2_name, player1_name, px, po
    if bns["text"] == " " and click_b is True:
        bns["text"] = "X"
        click_b = False
        px = p1.get() + " Won!"
        po = p2.get() + " Won!"
        checkForWin()
        button_clicked += 1
    elif bns["text"] == " " and click_b is False:
        bns["text"] = "O"
        click_b = True
        checkForWin()
        button_clicked += 1
    else:
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "Button already Clicked!")


def checkForWin():
    if (b1['text'] == b2['text'] == b3['text'] == 'X' != " " or
            b4['text'] == b5['text'] == b6['text'] == 'X' != " " or
            b7['text'] == b8['text'] == b9['text'] == 'X' != " " or
            b1['text'] == b4['text'] == b7['text'] == 'X' != " " or
            b2['text'] == b5['text'] == b8['text'] == 'X' != " " or
            b3['text'] == b6['text'] == b9['text'] == 'X' != " " or
            b1['text'] == b5['text'] == b9['text'] == 'X' != " " or
            b3['text'] == b5['text'] == b7['text'] == 'X' != " "):
        disableButton()
        tkinter.messagebox.showinfo("Tic-Tac-Toe", px)

    elif (b1['text'] == b2['text'] == b3['text'] == 'O' != " " or
            b4['text'] == b5['text'] == b6['text'] == 'O' != " " or
            b7['text'] == b8['text'] == b9['text'] == 'O' != " " or
            b1['text'] == b4['text'] == b7['text'] == 'O' != " " or
            b2['text'] == b5['text'] == b8['text'] == 'O' != " " or
            b3['text'] == b6['text'] == b9['text'] == 'O' != " " or
            b1['text'] == b5['text'] == b9['text'] == 'O' != " " or
            b3['text'] == b5['text'] == b7['text'] == 'O' != " "):
        disableButton()
        tkinter.messagebox.showinfo("Tic-Tac-Toe", po)

    elif button_clicked == 8:
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "Draw!! Try next time")


def restart_game():
    global click_b, button_clicked, player2_name, player1_name, px, po
    px = StringVar()
    po = StringVar()
    p3 = StringVar()
    p4 = StringVar()

    player1_name = Entry(tk, textvariable=p3, bd=5, width=20)
    player1_name.grid(row=0, column=1, columnspan=5)
    player2_name = Entry(tk, textvariable=p4, bd=5, width=20)
    player2_name.grid(row=1, column=1, columnspan=5)

    click_b = True
    button_clicked = 0

    b1.config(bg='black', text=' ', state=NORMAL)
    b2.config(bg='black', text=' ', state=NORMAL)
    b3.config(bg='black', text=' ', state=NORMAL)
    b4.config(bg='black', text=' ', state=NORMAL)
    b5.config(bg='black', text=' ', state=NORMAL)
    b6.config(bg='black', text=' ', state=NORMAL)
    b7.config(bg='black', text=' ', state=NORMAL)
    b8.config(bg='black', text=' ', state=NORMAL)
    b9.config(bg='black', text=' ', state=NORMAL)


buttons = StringVar()

l1 = Label(tk, text="Player1 is 'X'", font='Times 15 bold', height=1, width=9)
l1.grid(row=0, column=1)

l2 = Label(tk, text="Player2 is 'O'", font='Times 15 bold', height=1, width=9)
l2.grid(row=1, column=1)

play_again_button = Button(tk, text='Restart the Game', font='Times 15 bold', bg='black', fg='gold', width=13, height=1, command=lambda: restart_game())
play_again_button.grid(row=0, column=3)

b1 = Button(tk, text=' ', height=5, width=10, font='Times 20 bold', bg='black', fg='gold', command=lambda: Click_btn(b1))
b1.grid(row=3, column=1)

b2 = Button(tk, text=' ', height=5, width=10, font='Times 20 bold', bg='black', fg='gold', command=lambda: Click_btn(b2))
b2.grid(row=3, column=2)

b3 = Button(tk, text=' ', height=5, width=10, font='Times 20 bold', bg='black', fg='gold', command=lambda: Click_btn(b3))
b3.grid(row=3, column=3)

b4 = Button(tk, text=' ', height=5, width=10, font='Times 20 bold', bg='black', fg='gold', command=lambda: Click_btn(b4))
b4.grid(row=4, column=1)

b5 = Button(tk, text=' ', height=5, width=10, font='Times 20 bold', bg='black', fg='gold', command=lambda: Click_btn(b5))
b5.grid(row=4, column=2)

b6 = Button(tk, text=' ', height=5, width=10, font='Times 20 bold', bg='black', fg='gold', command=lambda: Click_btn(b6))
b6.grid(row=4, column=3)

b7 = Button(tk, text=' ', height=5, width=10, font='Times 20 bold', bg='black', fg='gold', command=lambda: Click_btn(b7))
b7.grid(row=10, column=1)

b8 = Button(tk, text=' ', height=5, width=10, font='Times 20 bold', bg='black', fg='gold', command=lambda: Click_btn(b8))
b8.grid(row=10, column=2)

b9 = Button(tk, text=' ', height=5, width=10, font='Times 20 bold', bg='black', fg='gold', command=lambda: Click_btn(b9))
b9.grid(row=10, column=3)

tk.mainloop()