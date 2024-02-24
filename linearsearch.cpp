#include <iostream>
using namespace std;

bool linear_search(int *arr,int size,int key){
    if (size==0){
        return false;}
    if (arr[0]==key){
        return true;
    }
    return linear_search(arr+1,size-1, key);
    };

void print(int arr[],int n){
    cout <<"Size of array is: "<<n<<endl;
    for (int i=0;i<n;i++){
        cout <<arr[i]<<" ";
    }
    cout <<endl;

}
int main(){
    int arr[]={1,2,3,4,5,6,7};
    int size=7;
    int key=55;
    print(arr,size);
    cout<<"Key is: "<<key<<endl;
    int ans=linear_search(arr,size,key);
    if (ans){
        cout<<"The element is present in the array"<<endl;
    }
    else{
        cout << "The element is not present in the array"<<endl;
    }
    return 0;
}