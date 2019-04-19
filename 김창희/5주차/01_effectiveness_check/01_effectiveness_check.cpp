// Problem URL -> https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV141176AIwCFAYD
// 정수 변수 만들어서 사용할때, 음수 범위를 쓸일이 없으면 int대신 size_t 사용하기

#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>

using namespace std;
 
vector<string>* split(const string& str, char delimiter);
bool is_digit(string str);				// 문자열이 숫자로 변환 가능한지 검사
void rtrim(string& str, const string& delimiters = " \f\n\r\t\v");
void ltrim(string& str, const string& delimiters = " \f\n\r\t\v");
void trim(string& str, const string& delimiters = " \f\n\r\t\v");

int main() {
	ifstream ifs;
	ifs.open("input.txt", ios_base::in);

	string temp;						// 파일을 입력받을 때 사용할 변수
	int num_of_nodes;				// 각 케이스별 노드의 개수
	for (int testcase = 1; testcase <= 10; testcase++) {
		/*
			입력은 완전 이진트리 이다.

			사칙연산이 유효할 조건
			1. 모든 노드는 자식이 없거나 둘이어야 함(즉, 총 노드의 개수는 짝수여야 함)
			2. 내부 노드의 data는 연산자여야 함
			3. 리프 노드의 data는 숫자여야 함
		*/

		// 노드의 개수 입력 받기
		getline(ifs, temp);
		trim(temp);
		num_of_nodes = atoi(temp.c_str());

	
		vector<string>* node_info;		// 각 노드의 정보
		vector<bool> data_is_digit_vector(num_of_nodes);		// 각 노드의 data가 숫자인지, 연산자인지를 저장한 벡터
																// 숫자일 경우 true, 연산자일 경우 false 저장
		

		for (int i = 0; i < num_of_nodes; i++) {
			// 각 노드의 정보 입력받기
			getline(ifs, temp);
			trim(temp);
			node_info = split(temp, ' ');

			data_is_digit_vector.at(i) = is_digit(node_info->at(1));
			delete node_info;
		}


		// 조건 1을 만족하지 못할 경우
		if (num_of_nodes % 2 == 0) {
			cout << "#" << testcase << " 0" << endl;
			continue;
		}


		// 첫번째 리프노드, 
		// 만약 총 노드의 개수가 1개(루트만 존재)일 경우, first_leaf_node = 0;
		int first_leaf_node = (num_of_nodes - 2) / 2 + 1; 
		
		bool effectiveness = true;		// 유효성
		

		// 조건 2를 만족하지 못할 경우
		for (int node_number = 0; node_number < first_leaf_node; node_number++) {
			if (data_is_digit_vector.at(node_number) == true) {
				effectiveness = false;
				break;
			}
		}

		if (!effectiveness) {
			cout << "#" << testcase << " 0" << endl;
			continue;
		}




		// 조건 3을 만족하지 못할 경우
		for (int node_number = first_leaf_node; node_number < num_of_nodes; node_number++) {
			if (data_is_digit_vector.at(node_number) == false) {
				effectiveness = false;
				break;
			}
		}
		
		if (!effectiveness) {
			cout << "#" << testcase << " 0" << endl;
			continue;
		}

		

		// 조건 1, 2, 3 모두 만족하면 유효한 사칙 연산
		cout << "#" << testcase << " 1" << endl;
		
		

		/*
		각 노드의 data가 숫자인지, 연산자인지를 저장한 벡터 출력
		
		vector<bool>::iterator iter;
		for (iter = data_is_digit_vector.begin(); iter != data_is_digit_vector.end(); iter++) {
			cout << *iter << " ";
		}
		cout << endl;
		*/
		

	}
	ifs.close();

	return 0;
}

bool is_digit(string str) {
	// str이 "0"인 경우도 고려
	return atoi(str.c_str()) != 0 || str.compare("0") == 0;
}

vector<string>* split(const string& str, char delimiter)
{
	vector<string>* tokens = new vector<string>();
	string token;

	istringstream tokenStream(str);
	while (getline(tokenStream, token, delimiter)) {
		tokens->push_back(token);
	}

	return tokens;
}


void rtrim(string& str, const string& delimiters) {
	size_t found = str.find_last_not_of(delimiters);
	if (found != string::npos) {
		str.erase(found + 1);
	}
	else {
		str.clear();
	}
}

void ltrim(string& str, const string& delimiters) {
	size_t found = str.find_first_not_of(delimiters);
	if (found != string::npos) {
		str.erase(0, found);
	}
	else {
		str.clear();
	}

}

void trim(string& str, const string& delimiters) {
	ltrim(str);
	rtrim(str);
}