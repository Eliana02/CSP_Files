import tkinter as tk
import string, dictionarylearning

root = tk.Tk()

def handle_login():
    print("Username:", ent_username.get())
    print("Password:", ent_password.get())

def handle_signup():
    if is_valid_password(ent_password.get()):
        result_label.config(text="That is valid")
        if ent_username.get() not in users:
            users[ent_username.get()] = ent_password.get()
        result_label.config(text="You are signed in")
    else:
        result_label.config(text="That is NOT valid")

    '''upper = False
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
    
    if len(ent_password.get()) >= 8:
        if lower and upper and digit and special:
            print("Username:", ent_username.get())
            print("Password:", ent_password.get())
            correct_label = tk.Label(root, text="Valid Password")
            correct_label.pack(pady=5)
    else:
        print("not valid")'''

def is_valid_password(password):
    if len(password) < 8:
        return False
    else:
        return True
    
    upper = False
    lower = False
    special = False
    digit = False

    for char in password:
        if char.islower:
            lower = True
        elif char.isupper:
            upper = True
        elif char.isdigit:
            digit = True
        elif char in string.punctuation:
            special = True
    
    return lower and upper and digit and special

root.geometry("300x250")
root.title("Authorization")

user_label = tk.Label(root, text="Username")
user_label.pack(pady=5)

ent_username = tk.Entry(root, bd=3)
ent_username.pack(pady=5)

pass_label = tk.Label(root, text="Password")
pass_label.pack(pady=5)

ent_password = tk.Entry(root, bd=3, show="*")
ent_password.pack(pady=5)

btn_login = tk.Button(root, text="Login", command=handle_login)
btn_login.pack(pady=5)

btn_signup = tk.Button(root, text="Sign Up", command=handle_signup)
btn_signup.pack(pady=5)

result_label = tk.Label(root, text="Result Label")
result_label.pack(pady=10)

root.mainloop()