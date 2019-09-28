#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

bool solution(vector<string> phone_book) {
    bool answer = true;

    sort(phone_book.begin(), phone_book.end());
    
    for ( int i = 0 ; i < phone_book.size()-1; i++){
        int tmp = 0;
        for ( int j = 0 ; j < phone_book[i].size(); j++){
            if(phone_book[i][j] == phone_book[i+1][j]) tmp++;
        }
        if (tmp == phone_book[i].size()) return false; 
    }
    return answer;
}

int main(){

    cout<<solution({"119", "97674223", "1195524421"})<<endl;
    cout<<solution({"123", "456", "789"})<<endl;
    cout<<solution({"12", "123", "1235", "567", "88"})<<endl;
}