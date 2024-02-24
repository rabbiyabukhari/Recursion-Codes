#include <iostream>
using namespace std;

int fib(int n){
    if (n==0 or n==1){
        return n;
    }
    int x1=0;
    int x2=1;
    int x;
    for (int i=0;i<n-1;i++){
        x=x1+x2;
        x1=x2;
        x2=x;
        
    }
    return x;

}
int main(){
    int n;
    cout << "Enter the number of the term you want to find out"<<endl;
    cin >> n;
    cout << fib(n)<< endl;

    return 0;
}