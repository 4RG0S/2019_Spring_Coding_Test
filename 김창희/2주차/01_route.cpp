//Problem URL -> https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14geLqABQCFAYD&&
#include <cstdio>

using namespace std;


void forward(const int *, const int *, int, bool&);			// 경로를 탐색하여, 목적지 까지의 길이 존재하는지 확인하는 함수

int main(){
	int test_number;					// 테스트 번호
	int number_of_order_pair;			// 순서쌍 개수

	for(int i = 1; i <= 10; i++){
		bool find = false;

		int route1[100] = {0, };		// 순서쌍 배열 1
		int route2[100] = {0, };		// 순서쌍 배열 2

		scanf("%d %d", &test_number, &number_of_order_pair);

		int start;		// 순서쌍에서 시작 점
		int end;		// 순서쌍에서 도착 점


		// 순서쌍 정보들을 순서쌍 배열 1과 2에 저장
		for(int i = 0; i < number_of_order_pair; i++){
			scanf("%d %d", &start, &end);

			if(route1[start] == 0){
				route1[start] = end;
			}else{
				route2[start] = end;
			}
		}


		// dynamic도 가능??	
		forward(route1, route2, 0, find);				// 출발점에서부터 탐색 시작

		printf("#%d %d\n", test_number, find);
		}

		return 0;
	}



void forward(const int * route1, const int * route2, int vertex, bool& find){
	if(find == true){				// 시간 절약 가능?
		return ;
	}

	if(vertex == 99){				// 목적지 까지의 길이 존재
		find = true;
		return;
	}


	if(route1[vertex] != 0){									// 첫 번째 경로가 존재하는 경우
		forward(route1, route2, route1[vertex], find);
	}

	if(route2[vertex] != 0){									// 두 번째 경로가 존재하는 경우
		forward(route1, route2, route2[vertex], find);
	}

}