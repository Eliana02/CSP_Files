from tkinter import *
import gdx
import matplotlib.pyplot as plt
import numpy as np

gdx = gdx.gdx()

def graph_data():

    with open(start_reading) as f:
        data = f.read().split("\n")
        print(data)

    red = []
    green = []
    blue = []

    for line in data:
        red.append(float(vals[0]))
        green.append(float(vals[1]))
        blue.append(float(vals[2]))

    time = np.arange(0,pers*seconds,1000//pers)

    fig, ax = plt.subplots(3, 1)

    plt.suptitle("Time v Light")
    plt.xlabel("Time")

    ax[0].plot(time, red, color="red")
    ax[1].plot(time, green, color="green")
    ax[2].plot(time, blue, color="blue")

    ax[0].set(ylabel="615 nm")
    ax[1].set(ylabel="525 nm")
    ax[2].set(ylabel="465 nm")

    plt.show()

def start_reading():
    seconds = int(seconds_field.get())
    pers = int(samples_field.get())
    print(seconds, pers)

    gdx.open_usb()
    gdx.select_sensors([5,6,7])
    gdx.start(period = 1000//pers) 

    for i in range(seconds * pers):
        measurements = gdx.read() #returns a list of measurements from the sensors selected.
        if measurements == None: 
            break 
        return(measurements)
    graph_data(start_reading)


root = Tk()

seconds_label = Label(root, text="How many seconds?")
seconds_label.pack()
seconds_field = Entry(root)
seconds_field.pack()

samples_label = Label(root, text="How many samples per second?")
samples_label.pack()
samples_field = Entry(root)
samples_field.pack()

start_button = Button(root, command = start_reading, text="Start Sensor")
start_button.pack()

root.mainloop()