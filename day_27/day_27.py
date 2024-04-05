from tkinter import *

window = Tk()
window.title("My GUI")
window.minsize(width=500, height=300)
window.config(padx=100, pady=100)

# Label
my_label = Label(text="New text", font=("Arial", 18, "bold"))
my_label.config(text="Hello, How are ya!")
my_label.grid(column=0, row=0)

# Button


def button_clicked():
    my_label.config(text=input.get())


button = Button(text="Click Me", command=button_clicked)
button.grid(column=0, row=1)

new_button = Button(text="button 2")
new_button.grid(column=2, row=0)

# Entry
input = Entry(width=10)
input.grid(column=3, row=2)


# # Text
# new_text = Text(height=5, width=30)
# new_text.pack()
# new_text.focus()
# new_text.insert(END, "Type your command here")
# print(new_text.get(1.0, END))
#
# # Spinbox
# spinbox = Spinbox(from_=0, to=10)
# spinbox.pack()
#
#
# # Check Button
# checked_state = IntVar()
# check_button = Checkbutton(text="is on?", variable=checked_state)
# checked_state.get()
# check_button.pack()
#
# # Radio Button
# radio1 = Radiobutton(text="Option1", value=1)
# radio2 = Radiobutton(text="Option2", value=2)
# radio1.pack()
# radio2.pack()
#
#
# # Scale
# def scale_used(value):
#     print(value)
#
#
# scale = Scale(from_=1, to=50, command=scale_used)
# scale.pack()
#
#
# # List Box
#
# def listbox_used(event):
#     # Gets current selection from listbox
#     print(listbox.get(listbox.curselection()))
#
#
# listbox = Listbox(height=4)
# fruits = ["Apple", "Pear", "Orange", "Banana"]
# for item in fruits:
#     listbox.insert(fruits.index(item), item)
# listbox.bind("<<ListboxSelect>>", listbox_used)
# listbox.pack()

window.mainloop()
