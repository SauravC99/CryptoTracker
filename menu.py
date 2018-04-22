from tkinter import *
import CryptoTracker.graph as graph

dict = {0 : 1,
        1 : 4,
        2 : 9,
        3 : 16,
        4 : 25,
        5 : 36,
        6 : 49,
        7 : 64}
def gui():
    #initialize the menu
    menu = Tk()
    menubar = Menu(menu)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Ethereum")
    filemenu.add_command(label="Bitcoin")
    filemenu.add_command(label="Litecoin")
    filemenu.add_command(label="Ripple")
    filemenu.add_command(label="Monaco")
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=menu.quit)
    menubar.add_cascade(label="Currency", menu=filemenu)
    #create a frame for the menu - can be used to organize later
    frame = Frame(menu, border = 10)
    frame.pack()
    #not sure why bottomframe is necessary yet
    bottomframe = Frame(menu)
    bottomframe.pack(side = BOTTOM)
    #create resolution and title
    menu.geometry('800x600')
    menu.title("Crypto Tracker")
    #create button that graphs dictionary on press
    button = Button(frame, text="Graph", bg='black', fg='white', command= lambda: graph.graph(dict))
    button.pack(side = LEFT)
    menu.config(menu=menubar)
    menu.mainloop()

gui()