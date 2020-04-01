import math

#input temperature
temp=int(input("Temperature is: "))
if temp>=0 and temp<=50:
    #input wind speed
    speed = int(input("Wind speed is: "))
    if speed>3 and speed<120:
        #calculate windchill
        wind = 35.74 + 0.6215 * temp + (0.4275 * temp - 35.75) * (math.pow(speed, 0.16))
        print("Wind chill is: ",wind)
    else:
        print("Enter correct values!")
else:
    print("Enter correct values!")