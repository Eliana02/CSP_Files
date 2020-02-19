import matplotlib.pyplot as plt

path = "data_files/sounddata.csv"

with open(path) as f:
    data = f.read().split("\n")
    print(data)

time = []
soundc = []
sounda = []

for line in data[1:]:
    vals = line.split(",")
    time.append(float(vals[0]))
    soundc.append(float(vals[1]))
    sounda.append(float(vals[2]))

#plt.plot(time, soundc, color="blue")
plt.plot(time, sounda, color="red")

plt.title("Time v Sound")
plt.xlabel("Sound")
plt.ylabel("Time")

plt.show()