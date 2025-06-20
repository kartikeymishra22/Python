import time

timstamp = time.strftime('%H:%M:%S')
def total():
    print(timstamp)
    hour = time.strftime('%H')
    print(hour)
    minute = time.strftime('%M')
    print(minute)
    second = time.strftime('%S')
    print(second)

total()