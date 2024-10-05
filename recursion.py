# def fac(n):
#     if n == 0:
#         return 1
#     else:
#         return n * fac(n - 1)

# n = int(input("Enter number to find factorial: "))
# print(f"The factorial of {n} is {fac(n)}")

# def fib(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
# n = int(input("Enter a number to find Fibonacci sequence: "))
# for i in range(n + 1):
#     print(fib(i), end=' ')
# print(f"\nThe fibnacci at {n} position is {fib(n)}")      

def fun(n): # Decimal to Binary conversion
    if n==0:
        return
    fun(int(n/2))
    print(n%2, end='')
fun(25)