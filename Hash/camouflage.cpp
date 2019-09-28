#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

bool compare(vector<string> a , vector<string> b){
    if (a[1] < b[1]) return true;
    return false;
}
int solution(vector<vector<string>> clothes) {
    int answer = 1;
    sort(clothes.begin(), clothes.end(), compare);
    vector<int> type;
    string tmp = clothes[0][1];
    int chk = 1;

    for ( int i = 1 ; i < clothes.size() ; i++){
        if (tmp != clothes[i][1]){
            tmp = clothes[i][1];
            type.push_back(chk+1);
            chk = 1;
        }else chk++;
    }
    type.push_back(chk+1);
    
    for ( int i = 0 ; i < type.size(); i++){
        answer *= type[i];
    }
    answer--;
    return answer;
}

int main(){
    cout<<solution({{"yellow_hat", "headgear"}, {"blue_sunglasses", "eyewear"}, {"green_turban", "headgear"}})<<endl;
    cout<<solution({{"crow_mask", "face"}, {"blue_sunglasses", "face"}, {"smoky_makeup", "face"}})<<endl;
    cout<<solution({{"sweater", "shirt"}, {"jeans", "pants"}});
}