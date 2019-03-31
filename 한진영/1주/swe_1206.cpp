#include <cstdio>
#include <iostream>
using namespace std;

int main() {

	int t, count; // 테스트케이스, 조망권 세대 수
	int *arr;

	for (int i = 0; i < 10; i++) {
		count = 0;
		scanf_s("%d", &t);
		arr = new int[t];

		for (int j = 0; j < t; j++) { // 배열 초기화
			scanf_s("%d", &arr[j]);
		}

		for (int k = 2; k < t - 2; k++) {
			for (int height = arr[k]; ; --height) {
				if (height > arr[k - 1] && height > arr[k + 1] && height > arr[k - 2] && height > arr[k + 2]) {
					count++;
				}
				else {
					break;
				}
			}
		}
		printf("#%d %d\n", (i + 1), count);
	}
	return 0;
}