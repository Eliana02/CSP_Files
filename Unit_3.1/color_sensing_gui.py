import tkinter as tk
import random as rand
import gdx
gdx = gdx.gdx()

root = tk.Tk()
root.wm_geometry("1200x600")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'black', 'white']

def rand_color():
    color = rand.choice(colors)
    color_label = tk.Label(root, text=('Your color is ' + color)).grid(row=0, column=1)
    canvas = tk.Canvas(root, width=300, height=300, bg=color).grid(row=1, column=1, rowspan=4)

def take_sample():
    gdx.open_usb()
    gdx.select_sensors([5,6,7])
    gdx.start(period=1)
    sample = gdx.read()
    print(sample)
    gdx.stop()
    gdx.close()

direction_label = tk.Label(root, text="Generate a color, then find that color").grid(row=0)
start_button = tk.Button(root, command = rand_color, text='Generate Color').grid(row=1)

sensor_label = tk.Label(root, text='Place sensor near color and click button').grid(row=2)
sensor_button = tk.Button(root, command=take_sample, text="Capture Color").grid(row=3)


root.mainloop()