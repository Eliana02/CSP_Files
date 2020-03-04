import gdx

seconds = int(input("How many seconds would you like: "))
pers = int(input("How many samples per second: "))

gdx = gdx.gdx()
gdx.open_usb()
gdx.select_sensors([5,6,7])
gdx.start(period = 1000//pers) 

for i in range(seconds * pers):
    measurements = gdx.read() #returns a list of measurements from the sensors selected.
    if measurements == None: 
        break 
    print(measurements)

gdx.stop()
gdx.close()