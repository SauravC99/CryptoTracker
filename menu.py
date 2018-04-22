import tkinter as tk
import CryptoTracker.graph as graph

# menubar = Menu(menu)
# filemenu = Menu(menubar, tearoff=0)
# filemenu.add_command(label="Ethereum")
# filemenu.add_command(label="Bitcoin")
# filemenu.add_command(label="Bitcoin Cash")
# filemenu.add_command(label="Ripple")
# filemenu.add_command(label="EOS")
# filemenu.add_separator()
# filemenu.add_command(label="Exit", command=menu.quit)
# menubar.add_cascade(label="Currency", menu=filemenu)

dict = {0 : 1,
        1 : 4,
        2 : 9,
        3 : 16,
        4 : 25,
        5 : 36,
        6 : 49,
        7 : 64}


class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class Bitcoin(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="Bitcoin (BTC)")
        label.pack(side="top", fill="both", expand=True)

class BitcoinCash(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="Bitcoin Cash (BCH)")
        label.pack(side="top", fill="both", expand=True)

class Ethereum(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="Ethereum (ETH)")
        label.pack(side="top", fill="both", expand=True)

class Ripple(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="Ripple (XRP)")
        label.pack(side="top", fill="both", expand=True)

class Eosio(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="Eosio (EOS)")
        label.pack(side="top", fill="both", expand=True)

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = Bitcoin(self)
        p2 = BitcoinCash(self)
        p3 = Ethereum(self)
        p4 = Ripple(self)
        p5 = Eosio(self)

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", padx = 10, pady=10, expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p4.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p5.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = tk.Button(buttonframe, text="Bitcoin", width = 20, height = 5, command=p1.lift)
        b2 = tk.Button(buttonframe, text="Bitcoin Cash", width = 20, height = 5, command=p2.lift)
        b3 = tk.Button(buttonframe, text="Ethereum", width = 20, height = 5, command=p3.lift)
        b4 = tk.Button(buttonframe, text="Ripple", width = 20, height = 5, command=p4.lift)
        b5 = tk.Button(buttonframe, text="Eosio", width = 20, height = 5, command=p5.lift)

        b1.pack(side="left")
        b2.pack(side="left")
        b3.pack(side="left")
        b4.pack(side="left")
        b5.pack(side="left")

        p1.show()

if __name__ == "__main__":
    root = tk.Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("1280x720")
    root.mainloop()



        #initialize the menu
        #menu = Tk()
        #menu.geometry('1280x720')
        #menu.title("Crypto Tracker")

        #create a frame for the menu - can be used to organize later
        #var = StringVar()

        #create button that graphs dictionary on press
        #button = Button(menu, text="Windowed graph", bg='black', fg='white', command= lambda: graph.graph(dict))
        #button.pack(pady = 30)

        #buttonLabel = Label(frame, textvariable=var, font=("Times New Roman", 20))
        #var.set("This is a currency")
        #buttonLabel.pack(side=TOP)

        #menu.config(menu=menubar)
        #menu.mainloop()



