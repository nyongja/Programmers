#include <string>
#include <vector>
#include <iostream>
#include <cstring>
using namespace std;

bool check[200];

void dfs(int cur, int cnt, int n, vector<vector<int>> computers) {
	check[cur] = true;
	for (int next = 0; next < n; next++) {
		if (!check[next] && computers[cur][next] == 1) {
			dfs(next, cnt, n, computers);
		}
	}
}

int solution(int n, vector<vector<int>> computers) {
	int answer = 0;

	for (int i = 0; i < n; i++) {
		if (check[i]) continue;
		dfs(i, ++answer, n, computers);
	}

	return answer;
}

int main() {
	vector<vector<int>> graph = { {1, 1, 0}, {1, 1, 0}, {0, 0, 1} };
	vector < vector<int>> graph1 = { {1, 1, 0}, {1, 1, 1}, {0, 1, 1} };

	cout << solution(3, graph) << '\n';
	memset(check, false, sizeof(check));
	cout << solution(3, graph1) << '\n';

	return 0;
}
