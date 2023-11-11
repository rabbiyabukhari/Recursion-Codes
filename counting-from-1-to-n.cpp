#include <iostream>
using namespace std;

void power(int n){
    if (n==0){
        return;}
    power(n-1);
    cout<< n<<endl;
}

int main() {
    int n;
    cin>>n;
    cout<<endl;
    power(n);
    
    return 0;
}
