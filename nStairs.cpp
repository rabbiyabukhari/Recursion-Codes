#include <iostream>
using namespace std;

int countDistinctWaysToClimbNStairs(long long nstairs){
    if (nstairs<0){
        return 0;
    }
    else if (nstairs==0){
        return 1;
    }
    int ans= countDistinctWaysToClimbNStairs(nstairs-1)+countDistinctWaysToClimbNStairs(nstairs-2);
    return ans;
    
}
int main(){
    long long n;
    cout <<"Enter value: ";
    cin >> n;
    cout << countDistinctWaysToClimbNStairs(n) << endl;
    return 0;
}