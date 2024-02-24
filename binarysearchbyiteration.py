def binarysearch(arr,key):
    i=0
    start=0
    end=len(arr)-1
    mid=(start+end)//2
    if arr[start]>key or arr[end]<key:
        return False
    while start<=end:
        mid=(start+end)//2
        if arr[mid]==key:
            return True
        elif arr[mid]>key:
            end=mid-1
        elif arr[mid]<key:
            start=mid+1
    return False
        
def main():
    arr=[1,2,3,4,5,7,10]
    key=10
    print(binarysearch(arr,key))
    
main()