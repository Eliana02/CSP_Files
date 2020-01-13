import tkinter as tk


def handle_press():
    if ent_username.get() == "hello":
        if ent_password.get() == "world":
            print("User logged in")
    else:
        print("Try again")

root = tk.Tk()

root.geometry("200x180")
root.title("Authorization")

user_label = tk.Label(root, text="Username")
user_label.pack(pady=5)

ent_username = tk.Entry(root, bd=3)
ent_username.pack(pady=5)

pass_label = tk.Label(root, text="Password")
pass_label.pack()

ent_password = tk.Entry(root, bd=3, show="*")
ent_password.pack(pady=5)

btn_login = tk.Button(root, text="Login", command=handle_press)
btn_login.pack()


root.mainloop()