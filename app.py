from tkinter import *

click_currency = 0


root = Tk()
root.title("Mitt program")
textBox = Label(root, text="Waffffleeeeeeeeees")
textBox.pack()

def show():
    click_currency =+ 1
    textBox.config(text=f"{click_currency}")

show_button = Button(root, text=click_currency, width=50, command=show)
show_button.pack()

button = Button(root, text="Quit program", width=50, command=root.destroy)
button.pack()
root.mainloop()
