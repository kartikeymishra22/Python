#include<iostream>
using namespace std;

int main(){
    int n;
    cout << "Enter a number: ";
    cin >> n;

    int toPrint = 1;
    for(int row = 0; row < n; row++){
        for(int col = 0; col<n; col++){
            cout<< toPrint << " ";
            toPrint++;
        }
        cout<< endl;
    }

    return 0;
}