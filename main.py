from tkinter import *


def button_clicked():
    new_text = number.get()
    km = int(new_text) * 1.609
    label_3.config(text=km)


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=500)
window.config(padx=100, pady=100)

# Entry
number = Entry(width=10)
number.insert(END, string="0")
number.grid(row=0, column=1)

# Label
label_1 = Label(text="Miles")
label_1.config(padx=20)
label_1.grid(row=0, column=2)

label_2 = Label(text="is equal to ")
label_2.grid(row=1, column=0)

label_3 = Label(text="0")
label_3.grid(row=1, column=1)

label_4 = Label(text="Km")
label_4.grid(row=1, column=2)

# Button
button = Button(text="Calculate", command=button_clicked)
button.grid(row=2, column=1)


window.mainloop()
