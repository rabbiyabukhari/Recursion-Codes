def fibonacci(x):
    x1=0;x2=1
    if x==0:
        return 0
    if x==1:
        return 1
    for i in range(x-1):
        x=x1+x2
        x1=x2
        x2=x
    return x
        
def main():
    n=4
    print(fibonacci(4))
        
main()