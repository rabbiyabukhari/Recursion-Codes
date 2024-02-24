def linear_search(lst,key):
    if len(lst)==0:
        return False
    if key==lst[0]:
        return True
    return linear_search(lst[1:],key)
    
def main():
    lst=[89,2,3,4,6,9]
    key=89
    print(linear_search(lst,key))
main()