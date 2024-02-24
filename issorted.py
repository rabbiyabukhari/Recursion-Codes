def is_sorted(lst):
    if len(lst)<=1:
        return True
    if lst[0]>lst[1]:
        return False
    return is_sorted(lst[1:])

def main():
    lst=[2,3,4,4]
    print(is_sorted(lst))
    
    
main()