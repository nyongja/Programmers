#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

struct Music{
    string type;
    int play;
    int num;
};

bool compare_g(Music a, Music b){
    if (a.type < b.type) {
        if(a.num > b.num) return true;
        else return false;
    }else if (a.type == b.type){
        if (a.play > b.play) return true;
        else return false;
    }else return false;
}

bool compare_p(Music a, Music b){
    if (a.play > b.play) return true;
    return false;
}

vector<int> solution(vector<string> genres, vector<int> plays) {
    vector<int> answer;
    vector<Music> music;
    Music tmp;
    for (int i = 0 ; i < genres.size() ; i++){
        tmp.type = genres[i];
        tmp.play = plays[i];
        tmp.num = i;
        music.push_back(tmp);
    }

    sort(music.begin(), music.end(), compare_g);
    //sort(music.begin(), music.end(), compare_p);

    for (int i = 0 ; i < music.size() ;i++){
        cout<<music[i].type<<" "<<music[i].play<<" "<<music[i].num<<endl;
    }
    string cur = music[0].type;
    answer.push_back(music[0].num);
    int chk = 1;
    for (int i = 1 ; i < music.size(); i++){
        if(music[i].type != cur){
            cur = music[i].type;
            chk = 1;
            answer.push_back(music[i].num);
        }else{
            chk++;
            if (chk == 2) answer.push_back(music[i].num);
        }
    }
    
    return answer;
}

int main(){
    vector<int> answer = solution({"classic", "pop", "classic", "classic", "pop"}, {500, 600, 150, 800, 2500});

    for (int i = 0 ; i < answer.size() ; i++)
        cout<<answer[i]<<" ";
    cout<<endl;
}