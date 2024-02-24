#include <iostream>
using namespace std;

void say_digits(int n,string arr[]){
    //base case
    if (n==0){
        return;}
    int digit=n% 10;
    n=n/10;
    say_digits(n,arr);
    //processing
    cout <<arr[digit] <<" ";};

int main(){
    int n=1089;
    string arr[10]={"zero","one","two","three","four","five","six","seven","eight","nine"};
    say_digits(n,arr);
    return 0;}