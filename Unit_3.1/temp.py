import matplotlib.pyplot as plt

path = "data_files/rawdata_311.csv"

with open(path) as f:
    data = f.read().split("\n")
    print(data)

time = []
temp1 = []
temp2 = []

#split into a list of lines
for line in data[1:]:
   vals = line.split(",")
   print(vals)
   #put each value in its respective list
   time.append(int(vals[0]))
   temp1.append(float(vals[1]))
   temp2.append(float(vals[2]))

plt.plot(time, temp1, color="blue")
plt.plot(time, temp2, color="violet")

plt.title("Time v Temperature")
plt.xlabel("Temperature")
plt.ylabel("Time(s)")

plt.show()