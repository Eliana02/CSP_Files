from tkinter import *
import gdx, matplotlib.pyplot as plt, numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

gdx = gdx.gdx()

def graph_data(seconds, pers, red, green, blue):

    plt.ion

    fig, ax = plt.subplots(3, 1)

    chart = FigureCanvasTkAgg(fig, root)

    time = np.arange(0,seconds,1/pers)

    #chart.suptitle("Time v Light")
    #chart.xlabel("Time")

    ax[0].plot(time, red, color="red")
    ax[1].plot(time, green, color="green")
    ax[2].plot(time, blue, color="blue")

    ax[0].set(ylabel="615 nm")
    ax[1].set(ylabel="525 nm")
    ax[2].set(ylabel="465 nm")

    chart.get_tk_widget().grid(row=0, column=1, columnspan=4, rowspan=5)

def start_reading():
    seconds = int(seconds_field.get())
    pers = int(samples_field.get())
    print(seconds, pers)

    gdx.start(period = 1000//pers) 
    red = []
    green = []
    blue = []

    for i in range(seconds * pers):
        vals = gdx.read() #returns a list of measurements from the sensors selected.
        if vals == None: 
            break 
        red.append(vals[0])
        green.append(vals[1])
        blue.append(vals[2])
        print(vals)

    graph_data(seconds, pers, red, green, blue)

root = Tk()

gdx.open_usb()
gdx.select_sensors([5,6,7])

seconds_label = Label(root, text="How many seconds?")
seconds_label.grid(row=0, sticky=W)
seconds_field = Entry(root)
seconds_field.grid(row=1)

samples_label = Label(root, text="How many samples per second?")
samples_label.grid(row=2, sticky=W)
samples_field = Entry(root)
samples_field.grid(row=3)

start_button = Button(root, command = start_reading, text="Start Sensor")
start_button.grid(row=4)

root.mainloop()