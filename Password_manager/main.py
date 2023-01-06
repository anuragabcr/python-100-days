from tkinter import *
from tkinter import messagebox
import pandas as pd
from password import gen_pass


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    pass_input.delete(0, END)
    pass_input.insert(0, gen_pass())


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    df = pd.read_csv(r"password.csv", index_col=0)
    web = web_input.get()
    email = email_input.get()
    pass_val = pass_input.get()
    if web and email and pass_val:
        save = messagebox.askokcancel(title="Confirmation: ", message=f" Email:{email}\n Password:{pass_val}\n Website:"
                                                                      f" {web} \n Do you want to save this ?")
        if save:
            df.loc[len(df)] = [web, email, pass_val]
            df.to_csv(r"password.csv")
            pass_input.delete(0, END)
            web_input.delete(0, END)
            web_input.focus()
    else:
        messagebox.showerror(title="Field Empty", message="You must fill all fields")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)

web_label = Label(text="Website: ")
web_label.grid(row=1, column=0)
email_label = Label(text="Email/Username: ")
email_label.grid(row=2, column=0)
pass_label = Label(text="Password: ")
pass_label.grid(row=3, column=0)

web_input = Entry(width=35)
web_input.grid(row=1, column=1, columnspan=2)
web_input.focus()
email_input = Entry(width=35)
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(0, "anuragibt@gmail.com")
pass_input = Entry(width=20)
pass_input.grid(row=3, column=1)

gen_button = Button(text="Generate Password", command=generate_password)
gen_button.grid(row=3, column=2)
add_button = Button(text="Add", width=30, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
