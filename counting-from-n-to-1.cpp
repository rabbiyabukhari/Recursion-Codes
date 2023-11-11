#include <iostream>
using namespace std;

void power(int n){
    if (n==0){
        return;}
    cout<< n<<endl;
    power(n-1);
}

int main() {
    int n;
    cin>>n;
    cout<<endl;
    power(n);
    
    return 0;
}
