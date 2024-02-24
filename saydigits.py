#say digits recursive solution where parameter n is string

def saydigits(n):
    nums=['zero','one','two','three','four','five','six','seven','eight','nine']
    if n=='':
        return ''
    return nums[int(n[0])]+' '+saydigits(n[1:])
  

def main():
    n=input('enter number: ')
    print(saydigits(n))
main()