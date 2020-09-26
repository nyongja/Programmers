#include <algorithm>
#include <string>
#include <vector>
using namespace std;

vector<int> solution(vector<int> array, vector<vector<int>> commands) {
    vector<int> answer;
    vector<int> tmp;
    for (int i = 0 ; i < commands.size() ; i++){
        tmp = array;
        sort(tmp.begin() + commands[i][0] - 1, tmp.begin() + commands[i][1]);
        answer.push_back(tmp[commands[i][0] + commands[i][2]-2]);
    }
    return answer;
}

int main(){
 
    vector<int> array = solution({1, 5, 2, 6, 3, 7, 4}, {{2, 5, 3}, {4, 4, 1}, {1, 7, 3}});
    for ( int i = 0 ; i < array.size(); i++){
        printf("%d", array[i]);
    }
}