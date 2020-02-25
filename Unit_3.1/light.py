import matplotlib.pyplot as plt

path = "data_files/light_sensor.csv"

with open(path) as f:
    data = f.read().split("\n")
    print(data)

time = []
red = []
green = []
blue = []

for line in data[1:]:
    vals = line.split(",")
    time.append(float(vals[0]))
    red.append(float(vals[1]))
    green.append(float(vals[2]))
    blue.append(float(vals[3]))

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