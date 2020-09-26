#include <string>
#include <vector>
#include <iostream>
#include <queue>
using namespace std;

queue <pair<int, int>> q;

int solution(vector<int> numbers, int target) {
    int answer = 0;
    
    pair<int, int>tmp = make_pair(0, 0);
    q.push(tmp);
    for ( int i = 0 ; i < numbers.size(); i++){
        while (tmp.second == i){
            //더하기
            q.push(make_pair(tmp.first+numbers[i], tmp.second+1));
            //빼기
            q.push(make_pair(tmp.first-numbers[i], tmp.second+1));
            tmp = q.front();
            q.pop();
        }
    }

    for ( int i = 0 ; i < q.size() ; i++){
        tmp = q.front();
        q.pop();
        if (tmp.first == target) answer++;
    }
    return answer;
}

int main(){
    cout << solution({1,1,1,1,1}, 3);
}