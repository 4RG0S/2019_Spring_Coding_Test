#include <iostream>
using namespace std;
int arr[16][16];
int visit[16][16];
int dx[4] = { 0,0,1,-1 };
int dy[4] = { 1,-1,0,0 };
bool flag = false;

void dfs(int x, int y)
{
	visit[x][y] = true;
	if (arr[x][y] == 3) {
		flag = true;
		return;
	}
	for (int i = 0; i < 4; i++) {
		int nx = x + dx[i];
		int ny = y + dy[i];
		if (nx >= 0 && ny >= 0 && nx < 16 && ny < 16) {
			if (!visit[nx][ny] && arr[nx][ny] != 1) {
				dfs(nx, ny);
			}
		}
	}
}
void init() {
	for (int i = 0; i < 16; i++) {
		for (int j = 0; j < 16; j++) {
			visit[i][j] = false;
		}
	}
	flag = false;
}
int main()
{
	int tc;
	for (int t = 0; t < 10; t++) {
		scanf("%d", &tc);
		for (int i = 0; i < 16; i++) {
			for (int j = 0; j < 16; j++) {
				scanf("%1d", &arr[i][j]);
			}
		}
		dfs(1, 1);
		if (flag) {
			printf("#%d %d\n", tc, 1);
		}
		else {
			printf("#%d %d\n", tc, 0);
		}
		init();
	}
}