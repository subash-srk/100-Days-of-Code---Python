# Mile to Km Converter

from tkinter import *

window = Tk()
# window.minsize(width=500, height=250)
window.title("Mile to Km Converter")
window.config(padx=50, pady=50)
FONT = ("Arial", 15, "normal")


def convert():
    miles = float(entry.get())
    km = round(miles * 1.609)
    val_label.config(text=f"{km}")


# Entry
entry = Entry(width=10)
entry.grid(column=1, row=0)

# Labels
mile_label = Label(text="Miles", font=FONT)
mile_label.grid(column=2, row=0)

is_label = Label(text="is equal to", font=FONT)
is_label.grid(column=0, row=1)

val_label = Label(text="0", font=FONT)
val_label.grid(column=1, row=1)

km_label = Label(text="Km", font=FONT)
km_label.grid(column=2, row=1)

# Button
button = Button(text="Calculate", command=convert)
button.grid(column=1, row=2)

window.mainloop()
