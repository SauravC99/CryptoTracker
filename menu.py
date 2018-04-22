#Nathan Gardner
import CryptoTracker.historicalPrice as price
import tkinter as tk
from tkinter import messagebox
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
                           command=lambda: graph.graph(price.currency("month", "BTC")))
        button.pack(side="left", padx=130, pady=50)
        button = tk.Button(self, text="Graph (1 Week)", bg="purple", fg="white", width=25, height=4,
                           command=lambda: graph.graph(price.currency("week", "BTC")))
        button.pack(side="left", padx=60, pady=50)
        button = tk.Button(self, text="Graph (1 Day)", bg="purple", fg="white", width=25, height=4,
                           command=lambda: graph.graph(price.currency("day", "BTC")))
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
        self.entry = tk.Entry(self, bd=10)
        phoneSubmitButton = tk.Button(self, text="Submit", command=self.onButton)
        phoneSubmitButton.pack(side="right", padx=10)
        self.entry.pack(side="right", anchor = "center")
        phoneLabel = tk.Label(self, text="Phone number")
        phoneLabel.pack(side="right", padx=25)

        dayPercentageLabel = tk.Label(self, text="1 day SMS: Default 10")
        dayPercentageLabel.pack(side="left", padx=25)
        self.entryPercentageDay = tk.Entry(self, bd=10)
        self.entryPercentageDay.pack(side="left", anchor="center")
        dayPercentageButton = tk.Button(self, text="Submit", command=self.onButtonDay)
        dayPercentageButton.pack(side="left", padx=10)

        minutePercentageLabel = tk.Label(self, text="5 minute SMS: Default: 1")
        minutePercentageLabel.pack(side="left")
        self.entryPercentageMinute = tk.Entry(self, bd=10)
        self.entryPercentageMinute.pack(side="left")
        minutePercentageButton = tk.Button(self, text="Submit", command=self.onButtonMinute)
        minutePercentageButton.pack(side="left")

    def validateNumber(self):
        messagebox.showerror("Error", "Phone number is not a valid length, enter an 11 digit phone number\n"
                                             "with country code. Example: 17146723892")

    def validatePercentage(self):
        messagebox.showerror("Error", "Percentage must be above 0 and only numbers. Example: 14")

    def onButtonMinute(self):
        try:
            percentage = self.entryPercentageMinute.get()
            percentageFloat = float(percentage)
            percentageString = str(percentageFloat)
            file = open("minutePercentage.txt", "w")
            file.write(percentageString)
            file.close()
        except ValueError:
            self.validatePercentage()

    def onButtonDay(self):
        try:
            percentage = self.entryPercentageDay.get()
            percentageFloat = float(percentage)
            percentageString = str(percentageFloat)
            file = open("dayPercentage.txt", "w")
            file.write(percentageString)
            file.close()
        except ValueError:
            self.validatePercentage()

    def onButton(self):
        number = self.entry.get()
        numberStrip = number.strip('.')
        if len(numberStrip) != 11:
            self.validateNumber()
        if len(numberStrip) == 11 and numberStrip.isnumeric() == True:
            file = open("phone.txt", "w")
            file.write(numberStrip)
            file.close()

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
        settingsContainer = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", padx = 10, pady=10, expand=False)
        container.pack(side="top", fill="both", expand=True)
        container2.pack(side="bottom", pady=10)
        settingsContainer.pack(side="right")

        #place the name of the button page in the middle of screen
        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p4.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p5.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p6.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p7.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        #button properties
        b1 = tk.Button(buttonframe, text="Bitcoin (BTC)", bg="orange", fg="white", width = 20, height = 5, command=p1.lift)
        b2 = tk.Button(buttonframe, text="Bitcoin Cash (BCH)", bg="green", fg="white", width = 20, height = 5, command=p2.lift)
        b3 = tk.Button(buttonframe, text="Ethereum (ETH)", bg="gray", fg="white", width = 20, height = 5, command=p3.lift)
        b4 = tk.Button(buttonframe, text="Ripple (XRP)", bg="blue", fg="white", width = 20, height = 5, command=p4.lift)
        b5 = tk.Button(buttonframe, text="Eosio (EOS)", bg="black", fg="white", width = 20, height = 5, command=p5.lift)
        b6 = tk.Button(container2, text="Menu", bg="gray", fg="white", width = 20, height = 5, command=p6.lift)
        b7 = tk.Button(settingsContainer, text="Settings", bg="gray", fg="white", width = 20, height = 5, command=p7.lift)

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




