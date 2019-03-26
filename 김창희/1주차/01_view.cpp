// problem URL -> https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV134DPqAA8CFAYh
#include <iostream>
#include <vector>

using namespace std;

int main(){
    for(int test_case = 1; test_case <= 10; test_case++){
        int result = 0;                             // 결과(조망권이 확보된 세대의 수)
        int building_num;							// 빌딩의 개수
	    cin >> building_num;
        vector<int> buildings(building_num, 0);		// 빌딩들을 담아둘 벡터
    
	    for(int i = 0; i < building_num; i++){			// 빌딩들의 정보를 벡터에 담기(빌딩의 개수 만큼)
           int temp;
          cin >> temp;
          buildings[i] = temp;    
      }
    
 
      for(int i = 2; i < building_num - 2; i++){
           int max_neighbor_building;		            // 인접 빌딩 중, 가장 높은 빌딩의 높이 
        
         if(buildings[i-2] >= buildings[i]){
                continue;
            }else{
                max_neighbor_building = buildings[i-2];
            }
            
            if(buildings[i-1] >= buildings[i]){
                continue;
            }else if(max_neighbor_building < buildings[i-1]){
                max_neighbor_building = buildings[i-1];
            }
                

            if(buildings[i+1] >= buildings[i]){
                continue;
            }else if(max_neighbor_building < buildings[i+1]){
                max_neighbor_building = buildings[i+1];
            }
            
            
            if(buildings[i+2] >= buildings[i]){
                continue;
            }else if(max_neighbor_building < buildings[i+2]){
                max_neighbor_building = buildings[i+2];
            }

            result += (buildings[i] - max_neighbor_building);		// 조망권이 확보된 세대의 수를 더하기
        }
        
        cout << "#" << test_case << " " << result << endl; 
    }
    return 0;
}
