try:
    import tkinter
except:
    import Tkinter as tkinter

keys = [[('C', 1), ('CE', 1)],
        [('7', 1), ('8', 1), ('9', 1), ('+', 1)],
        [('4', 1), ('5', 1), ('6', 1), ('-', 1)],
        [('1', 1), ('2', 1), ('3', 1), ('*', 1)],
        [('0', 1), ('=', 2), ('/', 1)]
        ]

rootPadding = 8

root = tkinter.Tk()
root.title("Calculator")
root.geometry("640x480-8-200")
root['padx'] = rootPadding

result = tkinter.Entry(root)
result.grid(row=0, column=0, sticky='nsew')

keyPad = tkinter.Frame(root)
keyPad.grid(row=1, column=0, sticky='nsew')

row = 0
for keyRow in keys:
    col = 0
    for key in keyRow:
        tkinter.Button(keyPad, text=key[0]).grid(row=row, column=col, columnspan=key[1], sticky=tkinter.E + tkinter.W)
        col += key[1]
    row += 1

root.update()
root.minsize(keyPad.winfo_width() + rootPadding, keyPad.winfo_height() + rootPadding + result.winfo_height())
root.maxsize(keyPad.winfo_width() + 50 + rootPadding, keyPad.winfo_height() + rootPadding + 50 + result.winfo_height())
root.mainloop()
