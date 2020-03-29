#include<iostream>

using namespace std;

int fours(int n){
    int count = 0;
    while(n > 0){
        if((n % 10) == 4){
            count++;
        }
        n = int(n/10);
    }
    return count;
}

int main(){

    int t, n;
    cin >> t;
    for(int i=0;i<t;i++){
        cin >> n;
        cout << fours(n) << endl;
    }

    return 0;
}
