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
        5 : 36}


class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class Bitcoin(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="Current Bitcoin Price")
        label.pack(side="top", pady=50)
        button = tk.Button(self, text="Graph (1 Month)", bg="purple", fg="white", width=25, height=4,
                           command=lambda: graph.graph(dict))
        button.pack(side="left", padx=130, pady=50)
        button = tk.Button(self, text="Graph (1 Week)", bg="purple", fg="white", width=25, height=4,
                           command=lambda: graph.graph(dict))
        button.pack(side="left", padx=60, pady=50)
        button = tk.Button(self, text="Graph (1 Day)", bg="purple", fg="white", width=25, height=4,
                           command=lambda: graph.graph(dict))
        button.pack(side="left", padx=130, pady=50)

class BitcoinCash(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="Current Bitcoin Cash Price")
        label.pack(side="top", pady=50)
        button = tk.Button(self, text="Graph (1 Month)", bg="purple", fg="white", width=25, height=4,
                           command=lambda: graph.graph(dict))
        button.pack(side="left", padx=130, pady=50)
        button = tk.Button(self, text="Graph (1 Week)", bg="purple", fg="white", width=25, height=4,
                           command=lambda: graph.graph(dict))
        button.pack(side="left", padx=60, pady=50)
        button = tk.Button(self, text="Graph (1 Day)", bg="purple", fg="white", width=25, height=4,
                           command=lambda: graph.graph(dict))
        button.pack(side="left", padx=130, pady=50)

class Ethereum(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="Current Ethereum Price")
        label.pack(side="top", pady=50)
        button = tk.Button(self, text="Graph (1 Month)", bg="purple", fg="white", width=25, height=4,
                           command=lambda: graph.graph(dict))
        button.pack(side="left", padx=130, pady=50)
        button = tk.Button(self, text="Graph (1 Week)", bg="purple", fg="white", width=25, height=4,
                           command=lambda: graph.graph(dict))
        button.pack(side="left", padx=60, pady=50)
        button = tk.Button(self, text="Graph (1 Day)", bg="purple", fg="white", width=25, height=4,
                           command=lambda: graph.graph(dict))
        button.pack(side="left", padx=130, pady=50)

class Ripple(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="Current Ripple Price")
        label.pack(side="top", pady=50)
        button = tk.Button(self, text="Graph (1 Month)", bg="purple", fg="white", width=25, height=4,
                           command=lambda: graph.graph(dict))
        button.pack(side="left", padx=130, pady=50)
        button = tk.Button(self, text="Graph (1 Week)", bg="purple", fg="white", width=25, height=4,
                           command=lambda: graph.graph(dict))
        button.pack(side="left", padx=60, pady=50)
        button = tk.Button(self, text="Graph (1 Day)", bg="purple", fg="white", width=25, height=4,
                           command=lambda: graph.graph(dict))
        button.pack(side="left", padx=130, pady=50)


class Eosio(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="Current Eosio Price")
        label.pack(side="top", pady=50)
        button = tk.Button(self, text="Graph (1 Month)", bg="purple", fg="white", width=25, height=4,
                           command=lambda: graph.graph(dict))
        button.pack(side="left", padx=130, pady=50)
        button = tk.Button(self, text="Graph (1 Week)", bg="purple", fg="white", width=25, height=4,
                           command=lambda: graph.graph(dict))
        button.pack(side="left", padx=60, pady=50)
        button = tk.Button(self, text="Graph (1 Day)", bg="purple", fg="white", width=25, height=4,
                           command=lambda: graph.graph(dict))
        button.pack(side="left", padx=130, pady=50)

class Home(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="Click any of the buttons to begin")
        label.pack(side="bottom", fill="both", expand=True)

class Settings(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        userInput = tk.Entry(self)
        userInput.pack(side="right")
        label = tk.Label(self, text="Phone number")
        label.pack(side="right")
        #add text input for phone number

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = Bitcoin(self)
        p2 = BitcoinCash(self)
        p3 = Ethereum(self)
        p4 = Ripple(self)
        p5 = Eosio(self)
        p6 = Home(self)
        p7 = Settings(self)

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
        p6.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        #button properties
        b1 = tk.Button(buttonframe, text="Bitcoin", bg="orange", fg="white", width = 20, height = 5, command=p1.lift)
        b2 = tk.Button(buttonframe, text="Bitcoin Cash", bg="green", fg="white", width = 20, height = 5, command=p2.lift)
        b3 = tk.Button(buttonframe, text="Ethereum", bg="gray", fg="white", width = 20, height = 5, command=p3.lift)
        b4 = tk.Button(buttonframe, text="Ripple", bg="blue", fg="white", width = 20, height = 5, command=p4.lift)
        b5 = tk.Button(buttonframe, text="Eosio", bg="black", fg="white", width = 20, height = 5, command=p5.lift)
        b6 = tk.Button(container2, text="Menu", bg="gray", fg="white", width = 20, height = 5, command=p6.lift)

        b1.pack(side="left", padx=40)
        b2.pack(side="left", padx=40)
        b3.pack(side="left", padx=40)
        b4.pack(side="left", padx=40)
        b5.pack(side="left", padx=40)
        b6.pack(side="bottom")

        menubar = tk.Menu(root)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Settings", command=p7.lift)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=root.quit)
        menubar.add_cascade(label="Settings", menu=filemenu)
        root.config(menu=menubar)

        p6.show()


if __name__ == "__main__":
    root = tk.Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.title("Crypto Tracker")
    root.wm_geometry("1280x720")
#
    root.mainloop()


