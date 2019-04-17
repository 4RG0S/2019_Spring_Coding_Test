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
void init_code_table(map<string, int>& code_table);		// 0 ~ 9�� ���� ��ȣ �ڵ� ���� �ʱ�ȭ�ϴ� �Լ�
void rtrim(string& str, const string& delimiters = " \f\n\r\t\v");
void ltrim(string& str, const string& delimiters = " \f\n\r\t\v");
void trim(string& str, const string& delimiters = " \f\n\r\t\v");

int main() {
	map<string, int> code_table;		// 0 ~ 9�� ���� ��ȣ �ڵ带 ������ ���̺�
	//char** password_code;			// ��ȣ�� ������ �迭

	string temp;					// ������ �Է¹��� �� ����� ����
	int number_of_testcase;			// �׽�Ʈ ���̽� ��

	// �׽�Ʈ ���̽� �� �Է¹ޱ�
	getline(cin, temp);
	trim(temp);
	number_of_testcase = atoi(temp.c_str());

	init_code_table(code_table);		// 0 ~ 9�� ���� ��ȣ �ڵ带 ������ map �ʱ�ȭ

	for (int testacase = 1; testacase <= number_of_testcase; testacase++) {
		int row_size, column_size;				// ��ȣ���� ����, ����ũ��
		getline(cin, temp);
		trim(temp);

		vector<int>* passsword_code_size = split(temp);		// �Է� ���� ���ڿ��� split(delimiter " ")�ؼ� ��ȣ���� ����, ���� ��
		row_size = passsword_code_size->at(0);
		column_size = passsword_code_size->at(1);
		delete passsword_code_size;


		/*
			// ��ȣ�� �迭 ����
			password_code = new char*[row_size];
			for (int i = 0; i < row_size; i++) {
				password_code[i] = new char[column_size + 1];
				getline(cin, temp);
				trim(temp);

				strcpy(password_code[i], temp.c_str());			// ���� ���ڿ� ��ȣ�� �迭�� ����
			}
			*/

			//�ص��� ������ �迭
		int decoded[8];
		fill_n(decoded, 8, 0);

		bool get_decoded = false;			// �ص��� ��ȣ���� ���´����� ���� ����
		for (int i = 0; i < row_size; i++) {
			getline(cin, temp);
			trim(temp);

			// �̹� ��ȣ�� ��������, ���� �б⸸ ��
			if (get_decoded) {
				continue;
			}

			size_t found = temp.find_last_not_of("0");
			if (found != string::npos) {
				int code_start_index = found + 6;

				/*
				// ��ȣ �ڵ尡 ���۵Ǵ� ���� ã��
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

					// ���������� ��ȣ�ڵ�
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


		int result = 0;		// �����
		int check = 0;		// ������
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
		// ��ȣ�� �迭�� ���� �޸� ����
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

