from tkinter import *

uppgradering = [
    {
        "name": "Våffel Järn"
    },
    {

    }
]
uppgradering.append('Click +1') #uppgradering = ['Klick +1']

root = Tk()
root.title("Mitt program")
textBox = Label(root, text="Waffle Clicker TM")
textBox.pack()

click_currency = 0
w = Label(root, text=click_currency)
w.pack()


def show():
    global click_currency
    click_currency += 1
    # textBox.config(text=f"{click_currency}")
    w.config(text=click_currency)

def show_upgrades():
    uppgradering.pop
    

show_button = Button(root, text="Klick för att tjäna", width=50, command=show)
show_button.pack()

button = Button(root, text="Quit program", width=50, command=root.destroy)
button.pack()
root.mainloop()
