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
    menu.geometry('1280x720')
    menu.title("Crypto Tracker")

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
    frame = Frame(menu)
    var = StringVar()
    frame.pack()

    #create button that graphs dictionary on press
    button = Button(menu, text="Windowed graph", bg='black', fg='white', command= lambda: graph.graph(dict))
    button.pack(pady = 30)

    buttonLabel = Label(frame, textvariable=var, font=("Times New Roman", 20))
    var.set("This is a currency")
    buttonLabel.pack(side=TOP)

    menu.config(menu=menubar)
    menu.mainloop()

gui()