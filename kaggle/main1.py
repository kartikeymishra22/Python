def least_difference(a,b,c):
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(c - a)
    return min(diff1, diff2, diff3)

print(
    least_difference(1,10,100),
    least_difference(1,10,10),
    least_difference(5,6,7),
)

