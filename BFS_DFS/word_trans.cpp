#include <string>
#include <vector>
#include <iostream>
#include <queue>
using namespace std;

queue<pair<string, int>> list;
bool check[50];

int solution(string begin, string target, vector<string> words) {
    pair<string, int> tmp;
    list.push(make_pair(begin, 0));
    while(!list.empty()){
        tmp = list.front();
        list.pop();
        for ( int i = 0 ; i < words.size() ; i++){
            int cnt = 0;
            if (!check[i]){
                for ( int j = 0 ; j < begin.length(); j++){
                    if (tmp.first[j] == words[i][j]) cnt++;    
                }

                if ( cnt == begin.length()-1 ){
                    if (words[i] == target) return tmp.second+1;
                    list.push(make_pair(words[i], tmp.second+1));
                    check[i] = true;
                }
            }
        }
    }
    return 0;
}

int main(){
    
    cout << solution("hit", "cog", {"hot", "dot", "dog", "lot", "log", "cog"}) << endl;
    cout << solution("hit", "cog", {"hot", "dot", "dog", "lot", "log"}) << endl;
}