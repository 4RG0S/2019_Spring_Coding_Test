// Problem URL -> https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15FZuqAL4CFAYD
#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <iterator>
#include <map>

using namespace std;

vector<int>* split(string str);
void init_code_table(map<string, int>& code_table);		// 0 ~ 9에 대한 암호 코드 맵을 초기화하는 함수
void rtrim(string& str, const string& delimiters = " \f\n\r\t\v");
void ltrim(string& str, const string& delimiters = " \f\n\r\t\v");
void trim(string& str, const string& delimiters = " \f\n\r\t\v");

int main() {
	map<string, int> code_table;		// 0 ~ 9에 대한 암호 코드를 저장할 테이블
	//char** password_code;			// 암호문 저장할 배열

	string temp;					// 파일을 입력받을 때 사용할 변수
	int number_of_testcase;			// 테스트 케이스 수

	// 테스트 케이스 수 입력받기
	getline(cin, temp);
	trim(temp);
	number_of_testcase = atoi(temp.c_str());

	init_code_table(code_table);		// 0 ~ 9에 대한 암호 코드를 저장할 map 초기화

	for (int testacase = 1; testacase <= number_of_testcase; testacase++) {
		int row_size, column_size;				// 암호문의 가로, 세로크기
		getline(cin, temp);
		trim(temp);

		vector<int>* passsword_code_size = split(temp);		// 입력 받은 문자열을 split(delimiter " ")해서 암호문의 가로, 세로 얻어냄
		row_size = passsword_code_size->at(0);
		column_size = passsword_code_size->at(1);
		delete passsword_code_size;


		/*
			// 암호문 배열 생성
			password_code = new char*[row_size];
			for (int i = 0; i < row_size; i++) {
				password_code[i] = new char[column_size + 1];
				getline(cin, temp);
				trim(temp);

				strcpy(password_code[i], temp.c_str());			// 읽은 문자열 암호문 배열에 대입
			}
			*/

			//해독문 저장할 배열
		int decoded[8];
		fill_n(decoded, 8, 0);

		bool get_decoded = false;			// 해독한 암호문을 얻어냈는지에 대한 여부
		for (int i = 0; i < row_size; i++) {
			getline(cin, temp);
			trim(temp);

			// 이미 암호문 얻어냈으면, 파일 읽기만 함
			if (get_decoded) {
				continue;
			}

			size_t found = temp.find_last_not_of("0");
			if (found != string::npos) {
				int code_start_index = found + 6;

				/*
				// 암호 코드가 시작되는 지점 찾기
				while (true) {
					if (code_table.find(temp.substr(code_start_index, 7)) != code_table.end()) {
						break;
					}
					code_start_index++;
				}
				*/

				int decoded_index = 7;
				while (decoded_index >= 0) {
					string code = temp.substr(code_start_index, 7);

					// 비정상적인 암호코드
					if (code_table.find(code) == code_table.end()) {
						code_start_index--;
						continue;
					}

					decoded[decoded_index] = code_table.at(code);
					decoded_index--;
					code_start_index -= 7;
				}

				get_decoded = true;
			}
		}


		int result = 0;		// 결과용
		int check = 0;		// 검증용
		for (int i = 0; i < 8; i++) {
			result += decoded[i];
			if (i % 2 == 0) {
				check += decoded[i] * 3;
			}
			else {
				check += decoded[i];
			}
		}

		if (check % 10 == 0) {
			cout << "#" << testacase << " " << result << endl;
		}
		else {
			cout << "#" << testacase << " 0" << endl;
		}

		/*
		// 암호문 배열에 대한 메모리 해제
		for (int i = 0; i < row_size; i++) {
			delete password_code[i];
		}
		delete password_code;
		*/
	}


	return 0;
}


vector<int>* split(string str) {
	istringstream iss(str);

	vector<int>* results = new vector<int>(istream_iterator<int>(iss), istream_iterator<int>());
	return results;
}

void init_code_table(map<string, int>& code_table) {
	code_table.insert(pair<string, int>("0001101", 0));
	code_table.insert(pair<string, int>("0011001", 1));
	code_table.insert(pair<string, int>("0010011", 2));
	code_table.insert(pair<string, int>("0111101", 3));
	code_table.insert(pair<string, int>("0100011", 4));
	code_table.insert(pair<string, int>("0110001", 5));
	code_table.insert(pair<string, int>("0101111", 6));
	code_table.insert(pair<string, int>("0111011", 7));
	code_table.insert(pair<string, int>("0110111", 8));
	code_table.insert(pair<string, int>("0001011", 9));
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

