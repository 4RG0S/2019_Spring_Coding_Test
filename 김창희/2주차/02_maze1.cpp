// Problem URL -> https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14vXUqAGMCFAYD&
#include <cstdio>
#include <iostream>

using namespace std;


// 미로의 각 지점에 대한 상태 구조체
typedef enum Status_t{
	Blocked = 0,
	Visited,
	Accesible
} Status;


void route(int (*maze)[16], Status (*maze_state)[16], int row, int col , bool& find);		// 미로를 탐색하여 출발 -> 도착 경로가 있는지 판단하는 함수
bool inside(int, int);					// 해당 포인트가 미로범위 안에 있는지 판단


int main(){
	int maze[16][16];					// 미로 배열
	Status maze_state[16][16];			// 미로의 각지점에 대한 상태를 저장하는 배열
	int testcase_number;

	for(int i = 0; i < 10; i++){
		cin >> testcase_number;
		


		// 미로 초기화 하는 방법 1
		string temp;		// 미로의 원소를 입력받을 임시 변수

		for(int row = 0; row < 16; row++){
			cin >> temp;
			for(int col = 0; col < 16; col++){
				maze[row][col] = (int)temp.at(col) - 48;

				// 미로의 각지점에 대한 상태 정보 저장
				if(maze[row][col] == 1){
					maze_state[row][col] = Blocked;
				}else{
					maze_state[row][col] = Accesible;
				}

			}
		}

	
/*
		// 미로 초기화 하는 방법 2
		char temp;			// 미로의 원소를 입력받을 임시 변수

		for(int row = 0; row < 16; row++){
			getchar();								// line feed 제거
			for(int col = 0; col < 16; col++){
				temp = getchar();
				maze[row][col] = (int)temp - 48;
			
				// 미로의 각지점에 대한 상태 정보 저장
				if(maze[row][col] == 1){
					maze_state[row][col] = Blocked;
				}else{
					maze_state[row][col] = Accesible;
				}

			}	
		}
*/

		bool find = false;				// 도착점까지의 길을 찾았는지 여부
		int start_row = 1;				// 시작 행
		int start_col = 1;				// 시작 열

		route(maze, maze_state, start_row, start_col, find);			// 정답 찾기!

		printf("#%d %d\n", testcase_number, find);
	}

	return 0;
}


void route(int (*maze)[16], Status (*maze_state)[16], int row, int col , bool& find){
	maze_state[row][col] = Visited;

	if(find == true){
		return;
	}

	if(maze[row][col] == 3){
		find = true;
		return;
	}


	if(inside(row, col - 1) && maze_state[row][col - 1] == Accesible){		// go to left
		route(maze, maze_state, row, col - 1, find);
	}

	if(inside(row - 1, col) && maze_state[row - 1][col] == Accesible){		// go to top
		route(maze, maze_state, row - 1, col, find);
	}

	if(inside(row, col + 1) && maze_state[row][col + 1] == Accesible){		// go to right
		route(maze, maze_state, row, col + 1, find);
	}

	if(inside(row + 1, col) && maze_state[row + 1][col] == Accesible){		// go to bottom
		route(maze, maze_state, row + 1, col, find);
	}

}


bool inside(int row, int col){
	if(row < 0 || row >= 16){
		return false;
	}

	if(col < 0 || col >= 16){
		return false;
	}

	return true;
}