try:
    x = int(input("Please enter a number : "))
except ValueError:
    print("Please enter an integer")

else:
    print("Integer accepted")

finally:
    print("this block is always executed")   