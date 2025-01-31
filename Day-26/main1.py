import time

timestamp = time.strftime('%Y-%m-%d %H:%M:%S')

hour = time.localtime().tm_hour


if hour < 12:
    print("Good morning!")

elif hour < 16:
    print("Good afternoon")

elif hour < 20:
    print("Good evening")

else:
    print("Good night")