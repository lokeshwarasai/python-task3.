def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact
x=int(input("enter a number: "))
fact=factorial(x)
print("Factorial of",x,"is",fact)
