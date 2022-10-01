from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=260, height=220, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(150, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Enteries
website_entry = Entry(width=23)
website_entry.grid(column=1, row=1)
website_entry.focus()
email_entry = Entry(width=40)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "email placeholder")
password_entry = Entry(width=23)
password_entry.grid(column=1, row=3)

# Buttons
search_button = Button(text="Search", width=12) #command=search_password
search_button.grid(column=2, row=1)
generate_password_button = Button(text="Generate Password" ) # command=generate_password
generate_password_button.grid(column=2, row=3)
add_button = Button(text="Add", width=30) # command=save
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()