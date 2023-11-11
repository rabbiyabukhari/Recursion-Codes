#include <iostream>
using namespace std;

void reachHome(int src,int dest){
    cout<<"Source: "<<src<<" Destination: "<<dest<<endl;
    if (src==dest){
        cout<<"reached Home";
        return;}
    //recursive call
    reachHome(src+1,dest);
}

int main() {
    int dest,src;
    cout<<"Please enter destination: ";
    cin>>dest;
    cout<<"Please enter source:";
    cin>>src;
    if ( src>dest ){
        cout << "Invalid input"<<endl;}
    
    else{
        reachHome(src,dest);}
        
    cout<<endl;
    return 0;
};