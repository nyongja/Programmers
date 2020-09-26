#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

string solution(vector<string> participant, vector<string> completion) {
    string answer = "";
    sort(participant.begin(), participant.end());
    sort(completion.begin(), completion.end());

    for (int i = 0 ; i < completion.size(); i++){
        if (participant[i] != completion[i]) return participant[i];
    }    
    return participant[participant.size()-1];
}

int main(){
    cout<<solution({"leo", "kiki", "eden"}, {"eden", "kiki"})<<endl;
    cout<<solution({"marina", "josipa", "nikloa", "vinko", "filipa"}, {"josipa", "filipa", "marina"
    , "nikola"})<<endl;
    cout<<solution({"mislav", "stanko", "mioslav", "ana"}, {"stanko", "ana", "mislav"})<<endl;   
}