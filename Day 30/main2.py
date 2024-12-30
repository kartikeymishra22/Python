# def fib(n,a=0,b=1):
#     if n == 0:
#         return a
#     else:
#         print(a,end=' ')
#     return fib(n-1,b,a+b)
    
# n = int(input())
# print(fib(n))

def fib(n,a=0,b=1):
    if(n==0):
        return a
    else:
        print(a,end=' ')
    return fib(n-1,b,a+b)

n = int(input("Enter the number of terms: "))
print(fib(n))