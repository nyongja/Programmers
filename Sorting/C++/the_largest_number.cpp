#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;

bool compare(string &a, string &b){

    if ( b + a < a + b) //둘이 합쳤을 때 a+b가 더 크게 되도록 정렬하겠다
        return true;
    return false;

}
string solution(vector<int> numbers) {
    string answer = "";
    vector<string> arr;

    for ( int i = 0 ; i < numbers.size(); i++){
        arr.push_back(to_string(numbers[i]));         
    }

    sort(arr.begin(), arr.end(), compare);

    for ( int i= 0 ; i< numbers.size(); i++){
        answer += arr[i];
    }

    if (answer[0] == '0')
        return "0";

    return answer;
}

int main(){
    cout << solution({6,10,2});
}