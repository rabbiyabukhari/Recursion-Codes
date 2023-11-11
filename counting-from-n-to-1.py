def counting(n):
    if n==0:
        return;
    print(n)
    counting(n-1)

def main():
    num=int(input())
    if num<=0:
        print("This function doesn't print counting for numbers less than 1")
    else:
        print()
        counting(num)
    
main()
