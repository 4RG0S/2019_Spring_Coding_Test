#include <stdio.h>

int edge[100][2]; // 정적배열 2개
int visit[100];

int dfs(int num){
	int ret = 0;
	visit[num] = 1;
	if (num == 99) { // 도착점
		return 1;
	}
	for (int i = 0; i < 2; i++) {
		int nv = edge[num][i];
		if (visit[nv] == 0) {
			ret += dfs(nv);
		}
	}
	return ret;
}

int solve(){
	for (int i = 0; i < 100; i++) {
		edge[i][0] = edge[i][1] = 0;
		visit[i] = 0;
	}
	int tc, N; // 테스트케이스, 길이 
	scanf("%d %d", &tc, &N);

	for (int i = 0; i < N; i++){
		int v1, v2;
		scanf("%d %d", &v1, &v2);
		if (edge[v1][0] == 0) { //첫번째 배열
			edge[v1][0] = v2;  
		}
		else {				    //두번째 배열
			edge[v1][1] = v2;
		}
	}
	return dfs(0);
}

int main(int argc, char* argv[]){
	for (int tc = 1; tc <= 10; tc++) {
		printf("#%d %d\n", tc, solve());
	}
	return 0;
}