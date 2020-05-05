#!/usr/bin/python3
# @author Ashley Perrin
# 4/27/2020
# CS 224 Python Project separate gui

import tkinter as tk
import term as amsearch
from PIL import ImageTk, Image

TK_SILENCE_DEPRECATION = 1                    # Gets rid of warning message about TK version
    # GUI Code Elements
win = tk.Tk()                                 # Creating tk window object
win.geometry("1000x600")                       # Setting width & height of window
win.title("BotShopp")                        # titling window
win.configure(bg = "grey")                    # sets window color grey
cur_display = 0

def send_input():
     global cur_display
     cur_display = cur_display +  1
     if(cur_display == 1):
         cur_display = 0
         output.delete("1.0", "end-1c")

     input = search.get("1.0","end-1c")
     #search.delete("1.0", "end-1c")
     search.insert("1.0", "Searching amazon please wait...")
     output_item = amsearch.main(1, input)
     search.delete("1.0", "end-1c")
     output.insert("1.0", output_item)

welcome = tk.Label(win,                           # Creating welcome label with specifications
    text = "Welcome to your Amazon personal shopper bot!\n Enter any item you'd like to search for:",
    font = "Ayuthaya 24",
    relief = "groove",
    bd = 5,
    width = 80,
    foreground = "white",
    background = "navy blue")
welcome.pack()

frame = tk.Frame(win,
    bg = "grey",
    height = 500,
    width = 100,
    relief = "groove",)

frame.pack(padx=5, pady=10)

search_button = tk.Button(frame,
    text = "Search",
    bd = 5,
    font = "Ayuthaya 17",
    relief = "raised",
    command = lambda: send_input())

search_button.pack(padx=5, pady=10, side=tk.LEFT)

search = tk.Text(frame,
    bg = "khaki",
    bd = 5,
    foreground = "black",
    font = "Ayuthaya 17",
    width = 55,
    height = 1,
    relief = "groove",
    )

search.pack(padx=5, pady=10, side=tk.LEFT)

output_frame = tk.Frame(win,
    bg = "gray",
    height = 500,
    width = 200,
    relief = "groove",)

output_frame.pack()

output= tk.Text(output_frame,
    bg = "white",
    bd = 5,
    foreground = "black",
    font = "Ayuthaya 17",
    #state='disabled',
    width = 100,
    height = 10,
    relief = "groove",
    )
output.pack(padx=5, pady=10, side=tk.LEFT)

load = Image.open("avail.png")
loadsized = load.resize((190,125))
render = ImageTk.PhotoImage(loadsized)
pane = tk.Label(win, image = render)
pane.image = render

pane.pack()

win.mainloop()                                 # Runs all aspects of gui`
