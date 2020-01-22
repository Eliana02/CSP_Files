import tkinter as tk
import string
from passlib.hash import pbkdf2_sha256

root = tk.Tk()

def hash_password(password):
    hash = pbkdf2_sha256.hash(ent_password.get())
    return(hash)

def check_password(password):
    if pbkdf2_sha256.verify(ent_password.get(), users[ent_username.get()]):
        return True

def handle_login():
    if ent_username.get() in users:
        if not check_password(ent_password.get()):
            result_label.config(text="That password is incorrect")
        else:
            result_label.config(text="You are signed in")
    else:
        result_label.config(text="That is not an account, please sign up")

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

def handle_signup():

    if is_valid_password(ent_password.get()):
        result_label.config(text="That is valid")
        if ent_username.get() not in users:
            users[ent_username.get()] = hash_password(ent_password.get())
            result_label.config(text="You are signed up")
        else:
            result_label.config(text="That username is taken")
    else:
        result_label.config(text="That is NOT valid")

users = {}

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