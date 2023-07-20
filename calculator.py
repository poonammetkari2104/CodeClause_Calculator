from tkinter import *


def click(event):
    global cvalue
    text = event.widget.cget("text")
    if text == "=":
        if cvalue.get().isdigit():
            value = float(cvalue.get())
        else:
            value = eval(screen.get())

            cvalue.set(value)
            screen.update()

    elif text == "C":
        cvalue.set("")
        screen.update()
    elif text == "Delete":
        current_value = cvalue.get()
        cvalue.set(current_value[:-1])
        screen.update()
    else:
        cvalue.set(cvalue.get() + text)
        screen.update()


root = Tk()
root.geometry("350x600")
root.title("Calculator")

cvalue = StringVar()
cvalue.set("")
screen = Entry(root, textvar=cvalue, font="times 20 bold")
screen.pack(fill=X, ipadx=4, pady=5, padx=5)
f = Frame(root, bg="black")
b = Button(f, text="7", padx=8, pady=8, font="times 22 bold")
b.pack(side=LEFT, padx=6, pady=6)
b.bind("<Button-1>", click)
b = Button(f, text="8", padx=8, pady=8, font="times 22 bold")
b.pack(side=LEFT, padx=6, pady=6)
b.bind("<Button-1>", click)
b = Button(f, text="9", padx=8, pady=8, font="times 22 bold")
b.pack(side=LEFT, padx=6, pady=6)
b.bind("<Button-1>", click)
f.pack()

f = Frame(root, bg="black")
b = Button(f, text="4", padx=8, pady=8, font="times 22 bold")
b.pack(side=LEFT, padx=6, pady=6)
b.bind("<Button-1>", click)
b = Button(f, text="5", padx=8, pady=8, font="times 22 bold")
b.pack(side=LEFT, padx=6, pady=6)
b.bind("<Button-1>", click)
b = Button(f, text="6", padx=8, pady=8, font="times 22 bold")
b.pack(side=LEFT, padx=6, pady=6)
b.bind("<Button-1>", click)
f.pack()

f = Frame(root, bg="black")
b = Button(f, text="1", padx=8, pady=8, font="times 22 bold")
b.pack(side=LEFT, padx=6, pady=6)
b.bind("<Button-1>", click)
b = Button(f, text="2", padx=8, pady=8, font="times 22 bold")
b.pack(side=LEFT, padx=6, pady=6)
b.bind("<Button-1>", click)
b = Button(f, text="3", padx=8, pady=8, font="times 22 bold")
b.pack(side=LEFT, padx=6, pady=6)
b.bind("<Button-1>", click)
f.pack()

f = Frame(root, bg="black")
b = Button(f, text="0", padx=7.5, pady=8, font="times 22 bold")
b.pack(side=LEFT, padx=6, pady=6)
b.bind("<Button-1>", click)
b = Button(f, text="+", padx=8, pady=8, font="times 22 bold")
b.pack(side=LEFT, padx=6, pady=6)
b.bind("<Button-1>", click)
b = Button(f, text="-", padx=6.5, pady=8, font="times 22 bold")
b.pack(side=LEFT, padx=9, pady=7)
b.bind("<Button-1>", click)
f.pack()

f = Frame(root, bg="black")
b = Button(f, text="*", padx=7, pady=8, font="times 22 bold")
b.pack(side=LEFT, padx=6, pady=6)
b.bind("<Button-1>", click)
b = Button(f, text="/", padx=10, pady=9, font="times 22 bold")
b.pack(side=LEFT, padx=6, pady=6)
b.bind("<Button-1>", click)
b = Button(f, text="%", padx=8, pady=8, font="times 18 bold")
b.pack(side=LEFT, padx=6, pady=6)
b.bind("<Button-1>", click)
f.pack()

f = Frame(root, bg="black")
b = Button(f, text="=", padx=8, pady=8, font="times 18 bold")
b.pack(side=LEFT, padx=7, pady=7)
b.bind("<Button-1>", click)
b = Button(f, text="Delete", padx=10, pady=10, font="times 18 bold")
b.pack(side=LEFT, padx=7, pady=7)
b.bind("<Button-1>", click)
b = Button(f, text="C", padx=8, pady=12, font="times 18 bold")
b.pack(side=LEFT, padx=7, pady=7)
b.bind("<Button-1>", click)
f.pack()
root.mainloop()
