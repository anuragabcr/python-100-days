from tkinter import *

window = Tk()
window.title("Calculator")
window.config(width=150, height=75, padx=10, pady=5)


def cal():
    km = float(miles.get())*1.60934
    lable3.config(text=str(km))


miles = Entry(width=10)
miles.grid(column=1, row=0)
lable1 = Label(text="Miles", font=("Arial", 10, "bold"))
lable1.grid(column=2, row=0)
lable2 = Label(text="is equal to:", font=("Arial", 10, "bold"))
lable2.grid(column=0, row=1)
lable3 = Label(text="0", font=("Arial", 10, "bold"))
lable3.grid(column=1, row=1)
lable4 = Label(text="KM", font=("Arial", 10, "bold"))
lable4.grid(column=2, row=1)
button = Button(text='Calculate', font=("Arial", 12, "bold"), command=cal)
button.grid(column=1, row=2)

window.mainloop()
