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

class Home(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="Homepage")
        label.pack(side="bottom", fill="both", expand=True)

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = Bitcoin(self)
        p2 = BitcoinCash(self)
        p3 = Ethereum(self)
        p4 = Ripple(self)
        p5 = Eosio(self)
        p6 = Home(self)

        #create frames for buttons
        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        container2 = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", padx = 10, pady=10, expand=False)
        container.pack(side="top", fill="both", expand=True)
        container2.pack(side="bottom", pady=10)

        #place the name of the button page in the middle of screen
        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p4.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p5.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p6.place(in_=container, x=0, y=1, relwidth=1, relheight=1)

        #button properties
        b1 = tk.Button(buttonframe, text="Bitcoin", bg="orange", fg="white", width = 20, height = 5, command=p1.show)
        b2 = tk.Button(buttonframe, text="Bitcoin Cash", bg="green", fg="white", width = 20, height = 5, command=p2.show)
        b3 = tk.Button(buttonframe, text="Ethereum", bg="gray", fg="white", width = 20, height = 5, command=p3.show)
        b4 = tk.Button(buttonframe, text="Ripple", bg="blue", fg="white", width = 20, height = 5, command=p4.lift)
        b5 = tk.Button(buttonframe, text="Eosio", bg="black", fg="white", width = 20, height = 5, command=p5.lift)
        b6 = tk.Button(container2, text="Menu", bg="gray", fg="white", width = 20, height = 5, command=p6.lift)

        b1.pack(side="left", padx=40)
        b2.pack(side="left", padx=40)
        b3.pack(side="left", padx=40)
        b4.pack(side="left", padx=40)
        b5.pack(side="left", padx=40)
        b6.pack(side="bottom")

        p6.show()

if __name__ == "__main__":
    root = tk.Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.title("Crypto Tracker")
    root.wm_geometry("1280x720")
    root.mainloop()


