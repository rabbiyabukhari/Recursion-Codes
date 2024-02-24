#include <iostream>
using namespace std;

int sum_of_array(int arr[],int size){
    if (size==0){
        return 0;
    }
    return arr[0]+sum_of_array(arr+1,size-1);
}
int main(){
    int arr[]={13};
    int size=1;
    cout<<"sum of array is"<< sum_of_array(arr,size);
    return 0;
}