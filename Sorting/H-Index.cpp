#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;

bool compare(int a, int b){
    if (a > b ) return true;
    return false;    
}
int solution(vector<int> citations) {
    sort(citations.begin(), citations.end(), compare);
    
    for ( int i = 0 ; i < citations.size(); i++){
        if ( i+1 == citations[i]) return i+1;
        else if ( i+1 > citations[i]) return i;
    }
    return citations.size();
}

int main(){
    cout << solution({3, 0, 6, 1, 5});  //3
    cout << solution({4, 0, 6, 1, 5});  //3
    cout << solution({0});
    cout << solution({10, 0});
    cout << solution({7,6,5,2,1,0});
    cout << solution({10,9,8,2,1});
    cout << solution({100});
    cout << solution({100,99});
}