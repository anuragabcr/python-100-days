from tkinter import *
from tkinter import messagebox
import pandas as pd
from password import gen_pass


# ---------------------------- Search PASSWORD  ------------------------------- #
def search_password():
    df = pd.read_csv(r"password.csv", index_col=0)
    web = web_input.get().capitalize()
    if web:
        result = df[df['website'] == web]
        if len(result):
            pass_input.delete(0, END)
            pass_input.insert(0, result['password'].values[0])
            email_input.delete(0, END)
            email_input.insert(0, result['email'].values[0])
            messagebox.showinfo(title=result['website'].values[0], message=f"User/email: {result['email'].values[0]}\n"
                                                                           f"Password: {result['password'].values[0]}")
        else:
            messagebox.showerror(title="Not Found", message="Password not found.\n Save or Search different.")
    else:
        messagebox.showerror(title="Field Empty", message="Enter website name to search")


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
            df.loc[len(df)] = [web.capitalize(), email, pass_val]
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

web_input = Entry(width=30)
web_input.grid(row=1, column=1)
web_input.focus()
email_input = Entry(width=30)
email_input.grid(row=2, column=1)
email_input.insert(0, "anuragibt@gmail.com")
pass_input = Entry(width=30)
pass_input.grid(row=3, column=1)

src_button = Button(text="Search Password", command=search_password)
src_button.grid(row=1, column=2)
gen_button = Button(text="Generate Password", command=generate_password)
gen_button.grid(row=3, column=2)
add_button = Button(text="Add", width=30, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
