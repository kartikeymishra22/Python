salary = int(input("Enter your salary : "))

if not 20000<salary<100000:
    raise ValueError("Salary is out of range")