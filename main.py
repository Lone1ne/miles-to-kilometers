from tkinter import *

def button_clicked():
    new_text = float(input.get())
    km = new_text * 1.609
    km_num.config(text=f"{km}")

window = Tk()
window.title("Miles To Kilometers")
window.minsize(width=100, height=50)
window.config(padx=20, pady=20)

input = Entry(width=7)
print(input.get())
input.grid(column=1, row=0)

#Label
miles = Label(text="Miles")
miles.grid(column=2, row=0)

#Label
kilom = Label(text="Km")
kilom.grid(column=2, row=1)

#Label
km_num = Label(text="0")
km_num.grid(column=1, row=1)

#Label
equal_to = Label(text="is equal to")
equal_to.grid(column=0, row=1)

#button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=3)

window.mainloop()