try:
    import tkinter
except ImportError:
    import Tkinter as tkinter

# --- MAIN WINDOW ---
root = tkinter.Tk()
root.title("Calculator")
root.geometry("400x400")
root['padx'] = 4

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)
root.columnconfigure(4, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=1)
root.rowconfigure(4, weight=1)
root.rowconfigure(5, weight=1)

# --- WIDGETS ---
# Result text area
result = tkinter.Entry(root)
result.grid(row=0, column=0, columnspan=4, sticky='nsew')

# Buttons
cButton = tkinter.Button(root, text="C")
ceButton = tkinter.Button(root, text="CE")
sevenButton = tkinter.Button(root, text="7")
eightButton = tkinter.Button(root, text="8")
nineButton = tkinter.Button(root, text="9")
plusButton = tkinter.Button(root, text="+")
fourButton = tkinter.Button(root, text="4")
fiveButton = tkinter.Button(root, text="5")
sixButton = tkinter.Button(root, text="6")
minusButton = tkinter.Button(root, text="-")
oneButton = tkinter.Button(root, text="1")
twoButton = tkinter.Button(root, text="2")
threeButton = tkinter.Button(root, text="3")
timesButton = tkinter.Button(root, text="*")
zeroButton = tkinter.Button(root, text="0")
equalsButton = tkinter.Button(root, text="=")
divideButton = tkinter.Button(root, text="/")

cButton.grid(row=1, column=0, sticky='nsew')
ceButton.grid(row=1, column=1, sticky='nsew')
sevenButton.grid(row=2, column=0, sticky='nsew')
eightButton.grid(row=2, column=1, sticky='nsew')
nineButton.grid(row=2, column=2, sticky='nsew')
plusButton.grid(row=2, column=3, sticky='nsew')
fourButton.grid(row=3, column=0, sticky='nsew')
fiveButton.grid(row=3, column=1, sticky='nsew')
sixButton.grid(row=3, column=2, sticky='nsew')
minusButton.grid(row=3, column=3, sticky='nsew')
oneButton.grid(row=4, column=0, sticky='nsew')
twoButton.grid(row=4, column=1, sticky='nsew')
threeButton.grid(row=4, column=2, sticky='nsew')
timesButton.grid(row=4, column=3, sticky='nsew')
zeroButton.grid(row=5, column=0, sticky='nsew')
equalsButton.grid(row=5, column=1, columnspan=2, sticky='nsew')
divideButton.grid(row=5, column=3, sticky='nsew')

# cButton.config(border=2, relief="raised")

root.update()
root.minsize(root.winfo_width(), root.winfo_height())
root.mainloop()
