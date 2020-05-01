# @author Ashley Perrin
# 4/27/2020
# CS 224 Python Project separate gui

import tkinter as tk


TK_SILENCE_DEPRECATION = 1                    # Gets rid of warning message about TK version
    # GUI Code Elements
win = tk.Tk()                                 # Creating tk window object
win.geometry("650x300")                       # Setting width & height of window
win.title("BotShoppa")                        # titling window
#win.color("grey")                            # Potential to set entire window background color, possibly a light grey ?

label = tk.Label(                             # Creating label with specifications
    text = "  Welcome to your Amazon personal shopper bot!  \n  Enter any item you'd like to search Amazon for in the box below.",
    font = "Calibri 22",
    relief = "raised",
    foreground = "white",
    background = "blue")

f = tk.Frame( win,
    bg = "gray",
    height = 100,
    width = 200,
    relief = "raised",
    )

u = tk.Entry(win,
    bg = "yellow",
    text = "Search:",
    font = "Calibri 17",
    width = 40,
    relief = "raised",)

un = tk.Entry(f,
    bg = "sky blue",
    relief = "raised",
    text = "Email Login:\nPassword:",
    font = "Calibri 15")

pw = tk.Entry(f,
    bg = "sky blue",
    relief = "raised",
    text = "Password:",
    font = "Calibri 15")

label.pack()                                  # Adding welcome label to window
u.pack()
f.pack()
un.pack()
pw.pack()
win.mainloop()                                 # Runs all aspects of gui`
