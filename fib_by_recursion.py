def fibonacci(n):
    if n==0:
        return 0
    if n==1:
        return 1
    x= fibonacci(n-1)+fibonacci(n-2)
    return x

x=7
print(fibonacci(x))