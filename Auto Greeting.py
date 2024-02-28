import time
t = time.strftime('%H:%M:%S')
hour =int(time.strftime('%H'))
hour = int(input("Enter the time in hours: "))
print("check if it lies under 25 because there are 24hrs in a day:", hour)
if(hour>=0 and hour<12):
    print("GOOD MORNING")
elif(hour<=12 and hour<17):
    print("GOOD AFTERNOON")    
elif(hour<=17 and hour<=19):
    print(" GOOD EVENING") 
else:
    print("GOOD NIGHT")       