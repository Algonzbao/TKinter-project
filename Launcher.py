import tkinter as tk
import tkinter.ttk as ttk
from glob import glob
import os

root = tk.Tk()
root.title("My Launcher")
root.configure(background = "gray")
#root.attributes("-fullscreen", True)
class Button:
    
    row = 0
    column = 0
    
    def __init__(self,text,func,arg,image=""):
        if image != "":
            image = tk.PhotoImage(file=image)
        root.rowconfigure(Button.row, weight=1, minsize=40)
        root.columnconfigure(Button.column, weight=1, minsize=40)
        self.button = tk.Button(
            root,
            text = text,
            image = image,
            borderwidth = 0,
            bg="gray",
            highlightthickness = 0,
            activebackground="black",
            compound=tk.LEFT,
            command=lambda: func(arg))
        self.button.grid(row=Button.row, column=Button.column, sticky = "nsew", padx = 0)
        self.button.image = image
        
        if Button.column < 3:
            Button.column += 1
        else:
            Button.column = 0
            Button.row += 1
            
sites = glob("*.site")
if sites != []:
    with open(sites[0]) as file:
        file = file.readlines()
    for line in file:
        x = line.strip()
        x = [f.strip() for f in x.split("#")]
        title, address, image = x
        Button(title, os.system, address, image="/home/pi/Downloads/" + image)
        
root.mainloop()
