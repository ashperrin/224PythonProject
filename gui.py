#!/usr/bin/python3
# @author Ashley Perrin
# 4/27/2020
# CS 224 Python Project separate gui

import tkinter as tk
import term as amsearch

TK_SILENCE_DEPRECATION = 1                    # Gets rid of warning message about TK version
    # GUI Code Elements
win = tk.Tk()                                 # Creating tk window object
win.geometry("1000x500")                       # Setting width & height of window
win.title("BotShopp")                        # titling window
win.configure(bg = "grey")                            # Potential to set entire window background color, possibly a light grey ?

cur_display = 0

def send_input():
     global cur_display
     cur_display =cur_display +  1
     if(cur_display == 1):
         cur_display =0
         output.delete("1.0", "end-1c")

     input = search.get("1.0","end-1c")
     #search.delete("1.0", "end-1c")
     search.insert("1.0", "Searching amazon please wait...")
     output_item = amsearch.main(1, input)
     search.delete("1.0", "end-1c")
     output.insert("1.0", output_item)

welcome = tk.Label(win,                           # Creating welcome label with specifications
    text = "  Welcome to your Amazon personal shopper bot!",
    font = "Calibri 22",
    relief = "raised",
    foreground = "white",
    background = "blue")
welcome.pack()

frame = tk.Frame(win,
    bg = "grey",
    height = 500,
    width = 100,
    relief = "raised",)

frame.pack(padx=5, pady=10)

search_button = tk.Button(frame,
    text = "Search",
    font = "Calibri 17",
    relief = "raised",
    command=lambda: send_input())

search_button.pack(padx=5, pady=10, side=tk.LEFT)

search = tk.Text(frame,
    bg = "white",
    foreground = "black",
    font = "Calibri 17",
    width = 40,
    height = 1,
    relief = "raised",
    )

search.pack(padx=5, pady=10, side=tk.LEFT)


login_frame = tk.Frame(frame,
    bg = "gray",
    height = 100,
    width = 200,
    relief = "raised",)

login_frame.pack(padx=5, pady=10, side=tk.RIGHT)

username = tk.Entry(login_frame,
    bg = "sky blue",
    relief = "raised",
    text = "Email Login:\nPassword:",
    font = "Calibri 15")

username.pack()

password = tk.Entry(login_frame,
   bg = "sky blue",
    relief = "raised",
    text = "Password:",
    font = "Calibri 15")

password.pack()


login = tk.Button(login_frame, text="Login")
login.pack()

output_frame = tk.Frame(win,
    bg = "gray",
    height = 500,
    width = 200,
    relief = "raised",)

output_frame.pack()

output= tk.Text(output_frame,
    bg = "white",
    foreground = "black",
    font = "Calibri 17",
    #state='disabled',
    width = 100,
    height = 10,
    relief = "raised",
    )
output.pack(padx=5, pady=10, side=tk.LEFT)


#f.pack()
#un.pack()

win.mainloop()                                 # Runs all aspects of gui`
