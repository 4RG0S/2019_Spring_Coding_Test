// Problem URL -> https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14eWb6AAkCFAYD

#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <vector>
#include <string>
#include <cstring>
#include <stack>

using namespace std;

void rtrim(string& str, const string& delimiters = " \f\n\r\t\v");
void ltrim(string& str, const string& delimiters = " \f\n\r\t\v");
void trim(string& str, const string& delimiters = " \f\n\r\t\v");
bool bracket_valid_test(stack<char>& stack, char bracket);		// 전달된 (닫는) bracket이 짝짓기에 유효한지 검사



int main() {


	string temp;					// 문자열 입력받을 때 이용되는 temp 변수
	char* input_data;				// string 타입으로 입력받은 괄호를 저장할 char 포인터(배열)
	for (int testcase_num = 1; testcase_num <= 10; testcase_num++) {
		bool valid = true;									// 유효성 여부

		getline(cin, temp);
		trim(temp);
		int bracket_length = atoi(temp.c_str());		// 괄호의 길이

		input_data = new char[bracket_length + 1];
		memset(input_data, 0, bracket_length + 1);

		getline(cin, temp);
		strcpy(input_data, temp.c_str());

		stack<char> stack;			// 괄호 짝짓기에 사용할 stack
		for (int i = 0; i < bracket_length; i++) {
			char bracket = input_data[i];

			switch (bracket) {
			case '(':
			case '[':
			case '{':
			case '<':
				stack.push(bracket);
				break;

			case ')':
			case ']':
			case '}':
			case '>':
				valid = bracket_valid_test(stack, bracket);
				break;
			default:
				valid = false;
				break;
			}

			if (valid == false) {
				break;
			}
		}

		cout << "#" << testcase_num << " " << valid << endl;

		delete input_data;
	}

	return 0;
}


bool bracket_valid_test(stack<char>& stack, char bracket) {
	if (stack.empty()) {				// 여는 괄호가 스택에 없는데, 닫는 괄호가 등장할 경우
		return false;
	}

	char poped_bracket = stack.top();
	stack.pop();

	if (bracket == ')') {
		if (poped_bracket == '(') {
			return true;
		}
		else {
			return false;
		}
	}

	if (bracket == ']') {
		if (poped_bracket == '[') {
			return true;
		}
		else {
			return false;
		}
	}

	if (bracket == '}') {
		if (poped_bracket == '{') {
			return true;
		}
		else {
			return false;
		}
	}

	if (bracket == '>') {
		if (poped_bracket == '<') {
			return true;
		}
		else {
			return false;
		}
	}

	return false;
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