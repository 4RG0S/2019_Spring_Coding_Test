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
bool bracket_valid_test(stack<char>& stack, char bracket);		// Àü´ÞµÈ (´Ý´Â) bracketÀÌ Â¦Áþ±â¿¡ À¯È¿ÇÑÁö °Ë»ç



int main() {
	
	string temp;					// ¹®ÀÚ¿­ ÀÔ·Â¹ÞÀ» ¶§ ÀÌ¿ëµÇ´Â temp º¯¼ö
	char* input_data;				// string Å¸ÀÔÀ¸·Î ÀÔ·Â¹ÞÀº °ýÈ£¸¦ ÀúÀåÇÒ char Æ÷ÀÎÅÍ(¹è¿­)
	for (int testcase_num = 1; testcase_num <= 10; testcase_num++) {
		bool valid = true;									// À¯È¿¼º ¿©ºÎ
	
		cin >> temp;
		trim(temp);
		int bracket_length = atoi(temp.c_str());		// °ýÈ£ÀÇ ±æÀÌ
		
		input_data = new char[bracket_length + 1];
		memset(input_data, 0, bracket_length + 1);	
		
		cin >> temp;
		strcpy(input_data, temp.c_str());
		
		stack<char> stack;			// °ýÈ£ Â¦Áþ±â¿¡ »ç¿ëÇÒ stack
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
	if (stack.empty()) {				// ¿©´Â °ýÈ£°¡ ½ºÅÃ¿¡ ¾ø´Âµ¥, ´Ý´Â °ýÈ£°¡ µîÀåÇÒ °æ¿ì
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