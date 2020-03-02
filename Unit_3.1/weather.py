import matplotlib.pyplot as plt

path = "data_files/weather.csv"

with open(path) as f:
    data = f.read().split("\n")
    print(data)

date = []
mean_temp = []
min_temp = []
max_temp = []
actual_precip = []
record_min = []
record_max = []

days = 0

for line in data[1:]:
    vals = line.split(",")
    date.append(days)
    mean_temp.append(float(vals[1]))
    min_temp.append(float(vals[2]))
    max_temp.append(float(vals[3]))

    actual_precip.append(float(vals[10]))
    record_min.append(float(vals[6]))
    record_max.append(float(vals[7]))
    days += 1

fig, ax = plt.subplots(2, 3)

plt.suptitle("Weather")

#Plotting
ax[0][0].plot(date, mean_temp, color="purple")
ax[0][1].plot(date, min_temp, color="blue")
ax[0][2].plot(date, max_temp, color="red")

ax[1][0].plot(date, actual_precip, color="cyan")
ax[1][1].plot(date, record_min, color="blue")
ax[1][2].plot(date, record_max, color="red")

#Labels
ax[0][0].set(ylabel="Mean temp (F)")
ax[0][1].set(ylabel="Min temp (F)")
ax[0][2].set(ylabel="Max temp (F)")

ax[1][0].set(ylabel="Actual precip (in)")
ax[1][1].set(ylabel="Record min (F)")
ax[1][2].set(ylabel="Record max (F)")

ax[1][1].set(xlabel="Days Since July First 2014")

plt.show()