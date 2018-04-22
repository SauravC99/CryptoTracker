from tkinter import *
from graph import *

dict = {0 : 1,
        1 : 4,
        2 : 9,
        3 : 16}
def gui():
    #initialize the menu
    menu = Tk()
    #create a frame for the menu - can be used to organize later
    frame = Frame(menu)
    #not sure why bottomframe is necessary yet
    bottomframe = Frame(menu)
    bottomframe.pack(side = BOTTOM)
    #create resolution and title
    menu.geometry('1920x1080')
    menu.title("Crypto Tracker")
    #create button that graphs dictionary on press
    button = Button(menu, text="Graph", bg='black', fg='white', command= lambda: graph(dict))
    button.pack(side = LEFT)
    menu.mainloop()

gui()