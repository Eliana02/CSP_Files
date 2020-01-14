import tkinter as tk


def handle_press():
    upper = False
    lower = False
    special = False
    digit = False
    
    for char in ent_password.get():
        if char.islower():
            lower = True
            print("is lower")
        elif char.isupper():
            upper = True
            print("is upper")
        elif char.isnumeric():
            digit = True
            print("is numeric")
        elif not char.isalnum():
            special = True
            print("is special")
    
    if len(ent_password.get()) == 8:
        if lower == upper == digit == special == True:
            print("Username:", ent_username.get())
            print("Password:", ent_password.get())
            correct_label = tk.Label(root, text="Valid Password")
            correct_label.pack()
    else:
        print("not valid")



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