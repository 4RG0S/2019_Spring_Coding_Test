// Problem URL -> https://www.acmicpc.net/problem/11729
#include <iostream>
#include <stdio.h>
//#include <cmath>

using namespace std;

void solution(int, int, int);

int main(){
	int n;		// 원판의 개수
	
	cin >> n;

	//cout << (int)pow(2, n) - 1 << endl;		// 하노이 탑의 최소 이동 횟수 -> 2^n - 1
	cout << (1 << n) - 1 << endl;				// 하노의 탑의 최소 이동 횟수 -> 2^n - 1
	solution(n, 1, 3);							// n개의 탑을 1번 장대에서 3번 장대로 옮긴다		

	return 0;
}

void solution(int n, int start, int end){
	if(n == 0){
		return;
	}

	solution(n - 1, start, 6 - start - end);	// 목적지 옆 장대에 n-1개의 탑 옮기기
	//cout << start << " " << end << endl;		// n번째 원판을 목적지 장대에 옮기기 -> 시간 초과 발생(cin, cout이 속도가 느린편이라고 함)
	printf("%d %d\n", start, end);				// n번째 원판을 목적지 장대에 옮기기
	solution(n - 1, 6 - start - end, end);		// 목적지 옆 장대에 옮겨 둔 n-1개의 탑을 목적지로 옮기기
}


