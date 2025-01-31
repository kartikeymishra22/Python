import time

timestamp = time.strftime("%H:%M:%S")
print(timestamp)

hour = time.localtime().tm_hour

if(hour <12):
    print("Good Morning")

elif(hour <18):
    print("Good Afternoon")

else:
    print("Good Evening")

