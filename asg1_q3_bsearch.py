def binary_search(start,end,list,key):
    mid=(start+end)//2
    if list[mid]==key:
        return True
    if start>=end:
        return False
    if key>list[end] or list[start]>key:
        return False
    if key<list[mid]:
        return binary_search(start,mid-1,list,key)
    else:
        return binary_search(mid+1,end,list,key)
    
def main():
    #test case 1
    list=[1,2,3,4,6,8,9,10]
    key=9 #is present should 
    print('test case 1 output: ',binary_search(0,6,list,key))#should return True
    
    #test case 2
    list=[1,2,3,4,6,8,10]
    key=9 #isn't present 
    print('test case 2 output: ',binary_search(0,5,list,key))#should return False
    
    #test case 3
    list=[2,3,4,6,8,9,10,20]
    key=25 #key bigger than all elements present, so isn't present 
    print('test case 3 output: ',binary_search(0,6,list,key))#should return False
    
    #test case 4
    list=[2,3,4,6,8,9,10,20]
    key=2 #is present
    print('test case 4 output: ',binary_search(0,7,list,key))#should return True  

main()