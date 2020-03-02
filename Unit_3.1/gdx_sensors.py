import gdx
gdx = gdx.gdx()

samples = input("How many samples would you like: ")
period = input("How many seconds: ")/1000

gdx.open_usb()
gdx.select_sensors([5,6,7])
gdx.start(period) 

for i in range(sample * period):
    measurements = gdx.read() #returns a list of measurements from the sensors selected.
    if measurements == None: 
        break 
    print(measurements)

gdx.stop()
gdx.close()