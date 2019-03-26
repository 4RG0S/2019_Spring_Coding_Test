// problem URL -> https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14ABYKADACFAYh
#include <iostream>
using namespace std;

int main(){
    int test_case_num = 0;
    int ladder[100][100];
    for(int i = 0; i< 10; i++){                         // 테스트 케이스 10번 반복
        cin >> test_case_num;
        int arrive;									    // 도착점
        int width_and_height_size = sizeof(ladder) / sizeof(ladder[0]);
        
        // 사다리 구성하기
        for(int row = 0; row < width_and_height_size; row++){
        	for(int col = 0; col < width_and_height_size; col++){
            	cin >> ladder[row][col];
                if(row == (width_and_height_size - 1) && ladder[row][col] == 2){
                	arrive = col;					    // 도착점의 열(사다리의 아래 -> 위로 탐색할 예정)
                }
            }
        }
        
        // direction -> left : 0, right : 1, top : 2
        int direction = 2;								// init direction -> top
        int result = 0;
        
        int row = width_and_height_size - 1;            // 사다리 세로로 탈때 이용되는 변수, 반대(아래 -> 위 방향)으로 탐색하므로 실행시간 효율 증가
        int col = arrive;								// 사다리 가로로 탈때 이용되는 변수
      
              
        while(true){
        	if(direction == 0){					        // 왼쪽 방향으로 이동
            	col--;

                // 왼쪽 방향으로 이동 끝, 다시 윗 방향으로 이동해야 함
                if(col == 0 || ladder[row][col - 1] == 0){
                	direction = 2;   
                }
                
            }else if(direction == 1){		        	// 우측 방향으로 이동
                col++;

                // 우측 방향으로 이동 끝, 다시 윗 방향으로 이동해야 함
           		if(col == (width_and_height_size - 1) || ladder[row][col + 1] == 0){
                    direction = 2;
                }
                
            }else{									    // 윗 방향으로 이동
            	row--;
                if(row == 0){					        // 도착, 사다리 타기 끝
				    result = col;				        // 지정된 도착점에 대응되는 출발점 x를 저장하고 반복문 종료
                    break;
        		}else{	    							// 윗 방향으로 이동했지만, 도착하지 않은 경우
                    
                	if((col - 1 >=0) && (ladder[row][col - 1] == 1)){					                    // 좌측 방향으로 이동 가능한 통로 등장, 좌측 방향으로 이동해야 함		
                    	direction = 0;
                    }else if((col + 1 <= (width_and_height_size - 1)) && (ladder[row][col + 1] == 1)){		// 우측 방향으로 이동 가능한 통로 등장, 우측 방향으로 이동해야 함
                     	direction = 1;
                    }
                }

       		}
        }
        
        cout << "#" << test_case_num << " " << result << endl;
    }
    
    return 0;
}