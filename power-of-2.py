def power(n):
    if n==0:
        return 1;
    return 2*power(n-1)

def main():
    num=int(input())
    if num<0:
        print("This function doesn't calculate value for power of 2 with negative exponents")
    else:
        print(power(num))
    
main()
