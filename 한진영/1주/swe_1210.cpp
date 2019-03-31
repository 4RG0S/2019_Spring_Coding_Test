#include <iostream>

int ladder[100][100];

void find(int x, int y, int tc) {
	while (y > 0) {
		if (x > 0 && ladder[x - 1][y]) {
			while (ladder[--x][y]);
			x++;
		}
		else if (x < 99 && ladder[x + 1][y]) {
			while (ladder[++x][y]);
			x--;
		}
		y--;
	}
	printf("#%d %d\n", tc, x);
}
int main() {

	int num;
	int x, y;
	for (int tc = 1; tc <= 10; tc++) {
		scanf("%d", &num);

		for (int i = 0; i < 100; i++) {  //사다리초기화 
			for (int j = 0; j < 100; j++) {
				scanf("%d", &ladder[j][i]);
				if (ladder[j][i] == 2) { // 도착점 좌표 찾기
					x = j;
					y = i;
				}
			}
		}
		find(x, y, tc);
	}
	return 0;
}