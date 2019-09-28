#include <string>
#include <vector>
#include <iostream>
#include<algorithm>
using namespace std;


vector<vector<string>> answer;
void dfs( vector<string> route, vector<vector<string>> tickets, bool check[]){

    for ( int i = 0 ; i < tickets.size(); i++){
        if(route[route.size()-1] == tickets[i][0] and !check[i]){
            route.push_back(tickets[i][1]);
            check[i] = true;
            if(route.size() == tickets.size()+1) {
                answer.push_back(route);
            }
            else dfs(route, tickets, check);
        }        
    }
}

vector<string> solution(vector<vector<string>> tickets){
    vector<string>route;
    for (int i = 0 ; i < tickets.size(); i++){
        bool check[10000] = {false, };
        if(tickets[i][0] == "ICN"){
            route.clear();
            route.push_back("ICN");
            route.push_back(tickets[i][1]);
            check[i] = true;
            dfs(route, tickets, check);   
        }
    }

    sort(answer.begin(), answer.end());
    return answer[0];
}

int main(){  
    //vector<string> answer = solution({{"ICN", "JFK"}, {"HND", "IAD"}, {"JFK", "HND"}});
    vector<string> answer2 = solution({{"ICN", "FFF"}, {"FFF", "ICN"}});
    vector<string> answer1 = solution({{"ICN", "SFO"}, {"ICN", "ATL"}, {"SFO", "ATL"}, {"ATL", "ICN"}, {"ATL", "SFO"}});
    for (int i = 0 ; i < answer2.size(); i++)
        cout<<answer2[i]<<" ";
}