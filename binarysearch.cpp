#include <iostream>
using namespace std;
void print(int arr[], int s, int e){
    for (int i=s;i<=e;i++){
        cout<<arr[i]<<" ";
    }
    cout<<endl;
}
bool binary_search(int *list,int start,int end,int key){
    cout<<endl;
    print(list,start,end);
    if (start>end){        
        return false;} 
    int mid=(start+end)/2;
    if (list[mid]==key){
        return true;}
    if (key>list[end] || list[start]>key){
        return false;}
    if (key<list[mid]){
        return binary_search(list,start,mid-1,key);}
    else{
        return binary_search(list,mid+1,end,key);}   
}

int main(){
    int arr[]={1,2,3,7,9,99};
    int s=0;
    int e=5;
    int key=999;
    int ans=binary_search(arr,s,e,key);
    if (ans){
        cout<<"Element is present in list"<<endl;
    }
    else{
        cout<<"Element is not present in list"<<endl;
    }
    return 0;
}