#say digits recursive solution where parameter n is number
def say_digits(n):
    lst=['zero','one','two','three','four','five','six','seven','eight','nine']
    if n==0:
        return ''
    return say_digits(n//10)+' '+lst[n%10]
def main():
    s=123
    print(say_digits(s))   
    print(say_digits(10))
    print(say_digits(34156))
main()