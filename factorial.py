def factorial(n):
    if n==0:
        return 1
    else:
        return n * factorial(n-1)



def main():
    
    num=int(input())
    if num < 0:
        print("Sorry, factorial does not exist for negative numbers")
    else:
        print("The factorial of", num, "is", factorial(num))


    
main()
