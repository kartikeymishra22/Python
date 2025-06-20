import time 

timestamp = time.strftime('%H:%M:%S')

hour = int(time.strftime('%H'))

if( hour < 12):
    print("Good morning!")

elif(hour  < 18):
    print("Good afternoon!")

elif(hour  < 22):
    print("Good evening!")

else:
    print("Good night!")

print(timestamp)