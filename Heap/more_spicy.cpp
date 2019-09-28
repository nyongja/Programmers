#include <string>
#include <vector>
#include <queue>
#include <iostream>
using namespace std;

int solution(vector<int> scoville, int K) {
    int answer = 0;

    priority_queue<int, vector<int>, greater<int>> pq(scoville.begin(), scoville.end());

    int lowest_s;
    int low_s;
    while (pq.top() < K){
        if(pq.size() == 1) return answer = -1;

        lowest_s = pq.top();
        pq.pop();

        low_s = pq.top();
        pq.pop();

        pq.push(lowest_s + low_s*2);

        answer++;
    }
    return answer;
}

int main(){
    cout<<solution({1, 2, 3, 9, 10, 12}, 7)<<endl;
}