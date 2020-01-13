import tkinter as tk


def btn_press():
    print(ent_username.get())

root = tk.Tk()

root.geometry("200x150")
root.title("Login Practice")


user_label = tk.Label(root, text="Username")

user_label.pack()


ent_username = tk.Entry(root, bd=3)

ent_username.pack(pady=5)


btn_login = root.Button(root, text="Login", command=btn_press)

btn_login.pack()

#username = ent_username.get()

#print(username)

root.mainloop()